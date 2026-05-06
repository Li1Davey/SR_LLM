#!/usr/bin/env python3
"""
plot_results.py — plot best-reward-over-iterations and best-reward-over-time
for one or more finished (or still-running) MCTS run.log files.

Usage
-----
Single run:
    python plot_results.py ~/workspace/scibench/results/kepler_001/

Compare runs:
    python plot_results.py ~/workspace/scibench/results/arrhenius_089a/ \\
                           ~/workspace/scibench/results/arrhenius_089b/

Glob:
    python plot_results.py ~/workspace/scibench/results/arrhenius_*/

Output
------
Two PNG files written next to the first run's log:
    reward_vs_iterations.png
    reward_vs_time.png
"""

import re
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_log(log_path: Path) -> dict:
    """
    Extract per-iteration reward and wall-clock timestamp from a run.log.

    The log prints two complementary things on every evaluated expression:
        \t reward R \t loss: L simp: ...
    and on every episode boundary:
        \tITER N/total...

    We track the running best reward and snapshot it at each ITER line.
    For time we parse the pympler SUMMARY block timestamps if present,
    but those are sparse — instead we use the line index as a proxy for
    time and scale it using the total elapsed time from the final line.
    """
    text  = log_path.read_text(errors='replace')
    lines = text.splitlines()

    label    = log_path.parent.name
    use_llm  = any('use_llm=True' in l or "'use_llm': True" in l
                   or ('use_llm' in l.lower() and 'true' in l.lower())
                   for l in lines[:80])

    # Elapsed total (seconds) — used to scale the time axis
    elapsed_sec = None
    m = re.search(r'MCTS ([\d.]+) mins', text)
    if m:
        elapsed_sec = float(m.group(1)) * 60.0

    # Per-iteration curve: (iteration, best_reward_so_far)
    iter_curve  = []   # [(iter, best_reward)]
    # Line-index curve used for time proxy: (line_index, best_reward_so_far)
    line_curve  = []   # [(line_idx, best_reward)]

    current_iter = 0
    running_best = None
    for idx, line in enumerate(lines):
        m = re.search(r'\bITER\s+(\d+)/', line)
        if m:
            current_iter = int(m.group(1))
            if running_best is not None:
                iter_curve.append((current_iter, running_best))
                line_curve.append((idx, running_best))
            continue
        # Match reward lines: "\t reward -5.34 \t loss: ..."
        m = re.search(r'\breward\s+([-\d.e+]+)\s', line)
        if m:
            v = float(m.group(1))
            if running_best is None or v > running_best:
                running_best = v

    # Convert line indices to seconds using elapsed_sec as a scale factor
    time_curve = []
    if line_curve and elapsed_sec:
        max_line = line_curve[-1][0] if line_curve else 1
        time_curve = [
            (idx / max_line * elapsed_sec, r)
            for idx, r in line_curve
        ]

    return {
        'label':       label,
        'use_llm':     use_llm,
        'iter_curve':  iter_curve,
        'time_curve':  time_curve,
        'elapsed_sec': elapsed_sec,
        'complete':    elapsed_sec is not None,
    }


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

COLORS = ['#185FA5', '#993C1D', '#0F6E56', '#534AB7', '#854F0B', '#A32D2D']


def _downsample(curve, n=500):
    if len(curve) <= n:
        return curve
    step = len(curve) / n
    return [curve[int(i * step)] for i in range(n)]


def _make_label(run):
    suffix = ' (LLM)' if run['use_llm'] else ''
    status = '' if run['complete'] else ' [running]'
    return run['label'] + suffix + status


def plot_reward_vs_iterations(runs, out_path: Path):
    fig, ax = plt.subplots(figsize=(9, 5))

    for i, run in enumerate(runs):
        curve = _downsample(run['iter_curve'])
        if not curve:
            continue
        xs = [pt[0] for pt in curve]
        ys = [pt[1] for pt in curve]
        ax.plot(xs, ys,
                color=COLORS[i % len(COLORS)],
                linewidth=1.5,
                label=_make_label(run))

    ax.set_xlabel('Iteration', fontsize=12)
    ax.set_ylabel('Best reward so far', fontsize=12)
    ax.set_title('Best reward vs iterations', fontsize=13, fontweight='normal')
    ax.legend(fontsize=10, framealpha=0.7)
    ax.grid(True, alpha=0.25, linewidth=0.5)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f'Saved: {out_path}')


def plot_reward_vs_time(runs, out_path: Path):
    has_data = any(run['time_curve'] for run in runs)
    if not has_data:
        print('No time data available (runs still in progress or no elapsed time found) '
              '— skipping reward_vs_time.png')
        return

    fig, ax = plt.subplots(figsize=(9, 5))

    for i, run in enumerate(runs):
        curve = _downsample(run['time_curve'])
        if not curve:
            continue
        xs = [pt[0] / 60.0 for pt in curve]   # convert to minutes
        ys = [pt[1] for pt in curve]
        ax.plot(xs, ys,
                color=COLORS[i % len(COLORS)],
                linewidth=1.5,
                label=_make_label(run))

    ax.set_xlabel('Time (minutes)', fontsize=12)
    ax.set_ylabel('Best reward so far', fontsize=12)
    ax.set_title('Best reward vs time', fontsize=13, fontweight='normal')
    ax.legend(fontsize=10, framealpha=0.7)
    ax.grid(True, alpha=0.25, linewidth=0.5)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f'Saved: {out_path}')


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    run_dirs = [Path(p).expanduser().resolve() for p in sys.argv[1:]]

    runs = []
    for rd in run_dirs:
        log = rd / 'run.log'
        if not log.exists():
            print(f'WARNING: no run.log in {rd} — skipping', file=sys.stderr)
            continue
        print(f'Parsing {log} ...')
        runs.append(parse_log(log))

    if not runs:
        print('No valid run directories found.', file=sys.stderr)
        sys.exit(1)

    out_dir = run_dirs[0]
    plot_reward_vs_iterations(runs, out_dir / 'reward_vs_iterations.png')
    plot_reward_vs_time(runs,       out_dir / 'reward_vs_time.png')


if __name__ == '__main__':
    main()
