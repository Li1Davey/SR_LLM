import numpy as np
import json
import os
from datetime import datetime


class DataX(object):
    def __init__(self, vars_range_and_types):
        """
        """
        list_of_samplers = json.loads(vars_range_and_types)
        self.data_X_samplers = []
        for one_sample in list_of_samplers:
            if one_sample['name'] == 'Uniform':
                self.data_X_samplers.append(UniformSampling(one_sample['range'], one_sample['only_positive']))
            elif one_sample['name'] == 'LogUniform':
                self.data_X_samplers.append(LogUniformSampling(one_sample['range'], one_sample['only_positive']))
            elif one_sample['name'] == 'IntegerUniform':
                self.data_X_samplers.append(IntegerSampling(one_sample['range'], one_sample['only_positive']))
            elif one_sample['name'] == 'LogUniform2d':
                self.data_X_samplers.append((LogUniformSampling2d(one_sample['range'], one_sample['only_positive'], one_sample['dim'])))

    def randn(self, sample_size):
        list_of_X = [one_sampler(sample_size) for one_sampler in self.data_X_samplers]
        X = np.stack(list_of_X, axis=-1)  # shape: (sample_size, num_vars)
        
        # --- curriculum: if using delta, X1 will be set to X0 + Δ, so don't waste time checking X0!=X1 ---
        use_delta = os.getenv("SCIBENCH_USE_DELTA", "0") == "1"

        # --- enforce separation between X0 and X1 (reject + resample; preserves X1 marginal) ---
        if (not use_delta) and X.shape[-1] >= 2 and os.getenv("SCIBENCH_ENSURE_X0_NE_X1", "0") == "1":
            eps_abs = float(os.getenv("SCIBENCH_XPAIR_EPS", "1e-12"))
            eps_rel = float(os.getenv("SCIBENCH_XPAIR_REL_EPS", "1e-6"))
            max_tries = int(os.getenv("SCIBENCH_XPAIR_MAX_TRIES", "200"))

            x0 = X[:, 0]
            x1 = X[:, 1]

            for _ in range(max_tries):
                thr = eps_abs + eps_rel * np.maximum(np.abs(x0), np.abs(x1))
                bad = np.abs(x1 - x0) <= thr
                if not np.any(bad):
                    break

                n_bad = int(np.sum(bad))
                # resample ONLY X1 where it's too close to X0
                x1[bad] = self.data_X_samplers[1](n_bad)

            # If it STILL fails (rare), do one last full resample of X1 and accept whatever happens.
            # Important: do NOT "push" values; that distorts the distribution.
            thr = eps_abs + eps_rel * np.maximum(np.abs(x0), np.abs(x1))
            bad = np.abs(x1 - x0) <= thr
            if np.any(bad):
                x1 = self.data_X_samplers[1](len(x1))

            X[:, 0] = x0
            X[:, 1] = x1

        # --- curriculum hook: interpret X[:, delta_idx] as Δ and set X1 = X0 + Δ ---
        if os.getenv("SCIBENCH_USE_DELTA", "0") == "1":
            base_idx = int(os.getenv("SCIBENCH_DELTA_BASE_IDX", "0"))
            delta_idx = int(os.getenv("SCIBENCH_DELTA_VAR_IDX", "1"))
            X[:, delta_idx] = X[:, base_idx] + X[:, delta_idx]

        # --- OPTIONAL: clamp after delta (ONLY if explicitly enabled) ---
            if os.getenv("SCIBENCH_DELTA_CLAMP", "0") == "1":
                sampler = self.data_X_samplers[delta_idx]
                lo, hi = sampler.range
                X[:, delta_idx] = np.clip(X[:, delta_idx], lo, hi)
        
        # --- optional: save generated X to disk ---
        if os.getenv("SCIBENCH_SAVE_X", "0") == "1":
            save_dir = os.getenv("SCIBENCH_SAVE_DIR", "")
            eq_file = os.getenv("SCIBENCH_EQ_FILE", "unknown_equation")
            run_tag = os.getenv("SCIBENCH_RUN_TAG", "run")

            if save_dir:
                os.makedirs(save_dir, exist_ok=True)

                ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                eq_base = os.path.splitext(os.path.basename(eq_file))[0]
                pid = os.getpid()

                out_path = os.path.join(save_dir, f"{ts}_{eq_base}_pid{pid}_{run_tag}_X.npy")
                np.save(out_path, X)

        return X

class DefaultSampling(object):
    def __init__(self, name, range, only_positive=False):
        self.name = name
        self.range = range
        self.only_positive = only_positive


class LogUniformSampling(DefaultSampling):
    def __init__(self, ranges, only_positive=False):
        super().__init__('LogUniform', ranges, only_positive)

    def __call__(self, sample_size):
        if self.only_positive:
            # x ~ U(0.1, 10.0)
            log10_min = np.log10(self.range[0])
            log10_max = np.log10(self.range[1])
            return 10.0 ** np.random.uniform(log10_min, log10_max, size=sample_size)
        else:
            # x ~ either U(0.0, 1.0) or U(-1.0, 0.) with 50% chance
            num_positives = sum(np.random.uniform(0.0, 1.0, size=sample_size) > 0.5)
            num_negatives = sample_size - num_positives
            log10_min = np.log10(self.range[0])
            log10_max = np.log10(self.range[1])
            pos_samples = 10.0 ** np.random.uniform(log10_min, log10_max, size=num_positives)
            neg_samples = -10.0 ** np.random.uniform(log10_min, log10_max, size=num_negatives)
            all_samples = np.concatenate([pos_samples, neg_samples])
            np.random.shuffle(all_samples)
            return all_samples

    def get_x_grid(self):
        if self.only_positive:
            return np.linspace(self.range[0], self.range[1], 10000)
        else:
            pos_grid = np.linspace(self.range[0], self.range[1], 5000)
            neg_grid = -np.linspace(self.range[0], self.range[1], 5000)
            all_grids = np.concatenate([neg_grid, pos_grid])
            return all_grids


class UniformSampling(DefaultSampling):
    def __init__(self, ranges, only_positive=False):
        super().__init__('Uniform', ranges, only_positive)

    def __call__(self, sample_size):
        if self.only_positive:
            # x ~ U(0.0, 1.0)
            return np.random.uniform(self.range[0], self.range[1], size=sample_size)
        else:
            num_positives = sum(np.random.uniform(0.0, 1.0, size=sample_size) > 0.5)
            num_negatives = sample_size - num_positives
            pos_samples = np.random.uniform(self.range[0], self.range[1], size=num_positives)
            neg_samples = -np.random.uniform(self.range[0], self.range[1], size=num_negatives)
            all_samples = np.concatenate([pos_samples, neg_samples])
            np.random.shuffle(all_samples)
            return all_samples


class IntegerSampling(DefaultSampling):
    def __init__(self, ranges, only_positive=False):
        ranges = [int(ranges[0]), int(ranges[1])]
        super().__init__('IntegerUniform', ranges, only_positive)

    def __call__(self, sample_size):
        if self.only_positive:
            # x ~ U(1, 100)
            return np.random.randint(self.range[0], self.range[1], size=sample_size)
        else:
            # x ~ either U(1, 100) or U(-100, -1) with 50% chance
            num_positives = sum(np.random.uniform(0.0, 1.0, size=sample_size) > 0.5)
            num_negatives = sample_size - num_positives
            pos_samples = np.random.randint(self.range[0], self.range[1], size=num_positives)
            neg_samples = -np.random.randint(self.range[0], self.range[1], size=num_negatives)
            all_samples = np.concatenate([pos_samples, neg_samples])
            np.random.shuffle(all_samples)
            return all_samples

    def get_x_grid(self):
        if self.only_positive:
            return np.arange(self.range[0], self.range[1])
        else:
            pos_grid = np.arange(self.range[0], self.range[1])
            neg_grid = -np.arange(self.range[0], self.range[1])
            all_grids = np.concatenate([neg_grid, pos_grid])
            return all_grids


class DefaultSampling2d(object):
    def __init__(self, name, range, only_positive=False, dim=(1, 1)):
        self.name = name
        self.range = range
        self.only_positive = only_positive
        self.dim = dim


class LogUniformSampling2d(DefaultSampling2d):
    def __init__(self, ranges, only_positive=False, dim=(1, 1)):
        super().__init__('LogUniform2d', ranges, only_positive, dim=dim)

    def __call__(self, sample_size):
        if self.only_positive:
            # x ~ U(0.0, 1.0)
            out= 0.4 + 0.02 * (np.random.uniform(self.range[0], self.range[1], size=(sample_size, self.dim[0], self.dim[1])) - 0.5)
            # print(out.shape)
            return out
        else:
            raise NotImplementedError
