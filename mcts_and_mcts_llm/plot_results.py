#!/usr/bin/env python3
"""
plot_results.py — visualise MCTS run logs.

Usage
-----
    python plot_results.py <run_dir_a> [run_dir_b ...]

  The first directory is treated as Pure_MCTS, the second as LLM_MCTS.
  Additional directories are labelled Run 3, Run 4, etc.

Output (written next to the first run's log)
--------------------------------------------
  hof_rank_progression.png   — HOF ranks vs iteration
  throughput_vs_time.png     — cumulative iterations vs wall-clock minutes
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


# ── Run labels ────────────────────────────────────────────────────────────────
# First run passed = Pure MCTS, second = LLM MCTS, rest generic.
def _display_label(run_index, complete):
    base = ["Pure MCTS", "LLM MCTS"][run_index] if run_index < 2 \
           else f"Run {run_index + 1}"
    return base if complete else f"{base} [running]"


# ── Colour palette ────────────────────────────────────────────────────────────
# Each run: (rank-1 colour, lower-rank colour)
PALETTE = [
    ("#185FA5", "#7AAFD4"),   # blue  — Pure MCTS
    ("#993C1D", "#D4785A"),   # rust  — LLM MCTS
    ("#0F6E56", "#3DB891"),
    ("#534AB7", "#9B94E0"),
    ("#854F0B", "#C9892E"),
]

# Line styles cycling for lower ranks — makes them clearly distinct even in B&W
RANK_STYLES = ['-', '--', '-.', ':', (0, (3, 1, 1, 1))]


# ── Log parsing ───────────────────────────────────────────────────────────────

_ITER_RE    = re.compile(r'\bITER\s+(\d+)/')
_REWARD_RE  = re.compile(r'\breward\s+([-\d.eE+]+)\s')
_LLM_RE     = re.compile(r'\[MCTS-LLM\].*?Expanded grammar with (\d+) new rules')
_ELAPSED_RE = re.compile(r'MCTS ([\d.]+) mins')
_HOF_RE     = re.compile(r"'reward'\s*:\s*([-\d.eE+]+)")


def parse_log(log_path: Path) -> dict:
    text  = log_path.read_text(errors='replace')
    lines = text.splitlines()

    elapsed_sec = None
    m = _ELAPSED_RE.search(text)
    if m:
        elapsed_sec = float(m.group(1)) * 60.0

    # Pass 1: raw timeline
    timeline      = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = _ITER_RE.search(line)
        if m:
            timeline.append(('iter', int(m.group(1)), i))
            i += 1; continue
        m = _REWARD_RE.search(line)
        if m:
            timeline.append(('reward', float(m.group(1))))
            i += 1; continue
        if _LLM_RE.search(line):
            timeline.append(('llm',))
            i += 1; continue
        if 'PRINT HOF' in line:
            hof_rewards = []
            j = i + 1
            while j < len(lines) and j < i + 60:
                hm = _HOF_RE.search(lines[j])
                if hm:
                    hof_rewards.append(float(hm.group(1)))
                if '=' * 10 in lines[j] and j > i + 1:
                    break
                j += 1
            if hof_rewards:
                timeline.append(('hof', hof_rewards))
            i = j; continue
        i += 1

    # Pass 2: reduce to per-iter summaries
    current_iter  = 0
    running_best  = None
    pending_llm   = False
    pending_hof   = []
    iter_events   = []
    llm_iters     = []
    iter_line_nos = []

    for ev in timeline:
        kind = ev[0]
        if kind == 'iter':
            iter_line_nos.append(ev[2])
            iter_events.append({
                'iter':        ev[1],
                'best_reward': running_best,
                'hof_rewards': list(pending_hof),
            })
            current_iter = ev[1]
            pending_llm  = False
        elif kind == 'reward':
            v = ev[1]
            if running_best is None or v > running_best:
                running_best = v
        elif kind == 'hof':
            pending_hof = sorted(ev[1], reverse=True)
        elif kind == 'llm':
            pending_llm = True
            llm_iters.append(current_iter)

    # HOF rank curves (up to 5)
    N_RANKS = 5
    rank_curves = defaultdict(list)
    last_hof = []
    for ev in iter_events:
        hof = ev['hof_rewards'] if ev['hof_rewards'] else last_hof
        last_hof = hof
        for rank in range(N_RANKS):
            v = hof[rank] if rank < len(hof) else None
            rank_curves[rank].append((ev['iter'], v))

    # Cumulative-iterations curve: (t_min, iter_count)
    cumul_curve = []
    if iter_line_nos and elapsed_sec:
        max_line = max(iter_line_nos)
        for ln, ev in zip(iter_line_nos, iter_events):
            cumul_curve.append((ln / max_line * elapsed_sec / 60.0, ev['iter']))

    # LLM event times (minutes)
    llm_times = []
    if iter_line_nos and elapsed_sec and llm_iters:
        max_line  = max(iter_line_nos)
        iter2line = {ev['iter']: ln for ev, ln in zip(iter_events, iter_line_nos)}
        for it in llm_iters:
            closest = min(iter2line.keys(), key=lambda k: abs(k - it))
            llm_times.append(iter2line[closest] / max_line * elapsed_sec / 60.0)

    return {
        'rank_curves': rank_curves,
        'cumul_curve': cumul_curve,
        'llm_iters':   llm_iters,
        'llm_times':   llm_times,
        'elapsed_sec': elapsed_sec,
        'complete':    elapsed_sec is not None,
        'n_ranks':     N_RANKS,
    }


# ── Helpers ───────────────────────────────────────────────────────────────────

def _downsample(curve, n=800):
    if len(curve) <= n:
        return curve
    idx = np.round(np.linspace(0, len(curve) - 1, n)).astype(int)
    return [curve[i] for i in idx]


def _strip_none(pts):
    return [(x, y) for x, y in pts if y is not None]


def _style_ax(ax, xlabel, ylabel, title):
    ax.set_xlabel(xlabel, fontsize=12, labelpad=8)
    ax.set_ylabel(ylabel, fontsize=12, labelpad=8)
    ax.set_title(title, fontsize=13, fontweight='semibold', pad=10)
    ax.grid(True, alpha=0.15, linewidth=0.5, color='#888')
    ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(labelsize=10)


_fmt_iter = ticker.FuncFormatter(lambda x, _: f'{int(x):,}')
_fmt_min  = ticker.FuncFormatter(lambda x, _: f'{x:.0f}')


# ── Figure 1: HOF rank progression ───────────────────────────────────────────

def build_hof_figure(runs, labels):
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#F7F8FA')
    ax.set_facecolor('#F7F8FA')

    rank_display = ["Rank 1", "Rank 2", "Rank 3", "Rank 4", "Rank 5"]
    # Rank 1 bold, lower ranks thinner; all fully opaque so lines stay distinct
    rank_lws  = [2.6, 1.8, 1.4, 1.1, 0.9]
    rank_alphas = [1.0, 0.85, 0.70, 0.58, 0.46]

    plotted = False
    for i, (run, label) in enumerate(zip(runs, labels)):
        c_base, c_light = PALETTE[i % len(PALETTE)]
        for rank in range(run['n_ranks']):
            pts = _downsample(_strip_none(run['rank_curves'][rank]))
            if not pts:
                continue
            xs, ys = zip(*pts)
            # Rank 1 uses base colour; lower ranks use light colour
            color     = c_base if rank == 0 else c_light
            linestyle = RANK_STYLES[rank % len(RANK_STYLES)]
            lbl = f"{label} — {rank_display[rank]}"
            ax.plot(xs, ys,
                    color=color,
                    linewidth=rank_lws[rank],
                    alpha=rank_alphas[rank],
                    linestyle=linestyle,
                    label=lbl,
                    zorder=3)
            plotted = True

        # Vertical dotted lines at LLM grammar expansions
        for it in run['llm_iters']:
            ax.axvline(it, color=c_base, linewidth=1.0,
                       linestyle=':', alpha=0.35, zorder=0)

    if plotted:
        # Legend: two columns (one per run) anchored to upper right,
        # outside the data area so it never overlaps curves
        ax.legend(fontsize=8.5, framealpha=0.90,
                  loc='upper right',
                  ncol=len(runs),
                  borderpad=0.8, labelspacing=0.4)
        if any(run['llm_iters'] for run in runs):
            ax.text(0.01, 0.01, "┊ = LLM grammar expansion",
                    transform=ax.transAxes,
                    fontsize=8, va='bottom', color='#666')
    else:
        ax.text(0.5, 0.5,
                "No HOF data\n(run with verbose=True or wait for completion)",
                transform=ax.transAxes, ha='center', va='center',
                fontsize=11, color='#888')

    _style_ax(ax, "Iteration", "Reward", "Hall-of-Fame rank progression")
    ax.xaxis.set_major_formatter(_fmt_iter)
    ax.set_ylim(bottom=0)   # y-axis anchored at 0

    fig.tight_layout(pad=1.6)
    return fig


# ── Figure 2: Throughput (cumulative iterations vs time) ─────────────────────

def build_throughput_figure(runs, labels):
    fig, ax = plt.subplots(figsize=(9, 5.5))
    fig.patch.set_facecolor('#F7F8FA')
    ax.set_facecolor('#F7F8FA')

    has_data = False
    for i, (run, label) in enumerate(zip(runs, labels)):
        c_base, _ = PALETTE[i % len(PALETTE)]
        curve = run['cumul_curve']
        if not curve:
            continue
        has_data = True
        ts, iters = zip(*curve)

        ax.plot(ts, iters,
                color=c_base,
                linewidth=2.4,
                label=label,
                zorder=3,
                solid_capstyle='round')

        # Endpoint label: elapsed time in minutes, placed beside the last point
        if run['elapsed_sec'] is not None:
            elapsed_min = run['elapsed_sec'] / 60.0
            # Offset left for the faster run (shorter x), right-ish for slower
            x_off = 6 if ts[-1] > max(r['cumul_curve'][-1][0]
                                       for r in runs
                                       if r['cumul_curve']) * 0.5 else -55
            ax.annotate(
                f"{elapsed_min:.0f} min",
                xy=(ts[-1], iters[-1]),
                xytext=(x_off, 4), textcoords='offset points',
                fontsize=9, color=c_base, fontweight='semibold',
            )

        # LLM expansion markers — small diamonds on the line, no arrows
        for t_llm in run['llm_times']:
            closest = min(range(len(ts)), key=lambda k: abs(ts[k] - t_llm))
            ax.scatter([ts[closest]], [iters[closest]],
                       color=c_base, s=70, zorder=5,
                       marker='D', edgecolors='white', linewidths=0.8,
                       label=None)

    if has_data:
        ax.legend(fontsize=10, framealpha=0.90, loc='upper left',
                  borderpad=0.9)
        if any(run['llm_times'] for run in runs):
            ax.text(0.01, 0.01, "◆ = LLM grammar expansion",
                    transform=ax.transAxes,
                    fontsize=8, va='bottom', color='#666')
    else:
        ax.text(0.5, 0.5,
                "Timing data unavailable\n(runs must be complete)",
                transform=ax.transAxes, ha='center', va='center',
                fontsize=11, color='#888')

    _style_ax(ax,
              "Wall-clock time (minutes)",
              "Cumulative iterations completed",
              "Throughput: iterations vs time")
    ax.xaxis.set_major_formatter(_fmt_min)
    ax.yaxis.set_major_formatter(_fmt_iter)
    ax.set_ylim(bottom=0)
    ax.set_xlim(left=0)

    fig.tight_layout(pad=1.6)
    return fig


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    run_dirs = [Path(p).expanduser().resolve() for p in sys.argv[1:]]
    runs, labels = [], []
    for idx, rd in enumerate(run_dirs):
        log = rd / 'run.log'
        if not log.exists():
            print(f"WARNING: no run.log in {rd} — skipping", file=sys.stderr)
            continue
        print(f"Parsing {log} …")
        run = parse_log(log)
        runs.append(run)
        labels.append(_display_label(idx, run['complete']))

    if not runs:
        print("No valid run directories found.", file=sys.stderr)
        sys.exit(1)

    out_dir = run_dirs[0]

    fig_hof = build_hof_figure(runs, labels)
    out_hof = out_dir / 'hof_rank_progression.png'
    fig_hof.savefig(out_hof, dpi=150)
    plt.close(fig_hof)
    print(f"Saved: {out_hof}")

    has_time = any(r['elapsed_sec'] is not None for r in runs)
    if has_time:
        fig_tp = build_throughput_figure(runs, labels)
        out_tp = out_dir / 'throughput_vs_time.png'
        fig_tp.savefig(out_tp, dpi=150)
        plt.close(fig_tp)
        print(f"Saved: {out_tp}")
    else:
        print("No elapsed-time data — throughput_vs_time.png skipped.")


if __name__ == '__main__':
    main()