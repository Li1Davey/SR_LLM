

def make_data_sample_distribution(dataX_sampling_type):
    _all_samplers = {
        'normal': lambda scale, batch_size: np.random.normal(loc=0.0, scale=scale, size=batch_size),
        'exponential': lambda scale, batch_size: np.random.exponential(scale=scale, size=batch_size),
        'uniform': lambda scale, batch_size: np.random.uniform(low=-np.abs(scale), high=np.abs(scale), size=batch_size),
        'laplace': lambda scale, batch_size: np.random.laplace(loc=0.0, scale=scale, size=batch_size),
        'logistic': lambda scale, batch_size: np.random.logistic(loc=0.0, scale=scale, size=batch_size)
    }
    assert dataX_sampling_type in _all_samplers, "Unrecognized noise_type" + dataX_sampling_type

    return _all_samplers[dataX_sampling_type]


class Feynman_dataloader(Dataloader):
    def __int__(self, dataset_family, true_program, batch_size, noise_type, noise_scale, metric_name):
        """
        dataset_family: symbolic_equation_evaluator-easy, symbolic_equation_evaluator-medium, symbolic_equation_evaluator-hard
        """
        super().__int__(dataset_family, true_program, batch_size, noise_type, noise_scale, metric_name)

    # def gen_X_randomly(self, input_dim, fixed_dims, scale=9.5, bias=0.5, **extra_params):
    #     dataset_kwargs = dict()
    #     sampling_objs = build_sampling_objs(extra_params.pop('sampling_objs')) if 'sampling_objs' in extra_params else None
    #     eq_instance = get_eq_obj(self.eq_name, sampling_objs=sampling_objs, **extra_params)
    #     # Generate tabular dataset
    #     dataset = eq_instance.create_dataset(self.batch_size)
    #     ############################
    #
    #
    #     # sampling_objs = build_sampling_objs(dataset_kwargs.pop('sampling_objs')) if 'sampling_objs' in dataset_kwargs else None
    #     # eq_instance = get_eq_obj(dataset_name, sampling_objs=sampling_objs, **dataset_kwargs)
    #     #
    #     # # Write out each split
    #     # fixed_column = [i for i in range(len(eq_instance.x))]
    #     # dataset = eq_instance.create_fixedcolumn_dataset(singlefile_sample_size, fixed_column)
    #     # return dataset
    #     return dataset


class SinCosInv_dataloader(Dataloader):
    def __int__(self, dataset_family, true_program, batch_size, noise_type, noise_scale, metric_name):
        """
        dataset_family: Inv, SinCos, SinCosInv
        """
        super().__int__(dataset_family, true_program, batch_size, noise_type, noise_scale, metric_name)

    # def gen_X_randomly(self, input_dim, fixed_dims, scale=9.5, bias=0.5, **extra_params):
    #     X = np.random.rand(self.batch_size, input_dim) * scale + bias
    #     if len(fixed_dims) != 0:
    #         X[:, fixed_dims] = X[0, fixed_dims]
    #     return X

class Control_variable_generator:
    pass


class random_generator:
    pass


class Active_learning_generator:
    pass


