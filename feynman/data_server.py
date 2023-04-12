import time
import zmq
import numpy as np
from feynman.datasets import sampling, physic_equations
from feynman.datasets.registry import get_eq_obj
from feynman.datasets.sampling import build_sampling_objs
import json


# call a million batch of dataset. compute the time.
# a class takes the input of a file, that a file is an equation.
# the class will return a batch of data, everytime it was queried.
# don't do the tcp version.
# create a offline version to bitbucket.org
#
# future competition.
# offline evaluation: that are not open.
# type of noise, rate of noise.

def _recv_X_send_y():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        #  Wait for next request from client
        message = socket.recv()
        data_X = np.frombuffer(message, dtype=float)
        print("Received request: %s" % data_X.shape)
        print(data_X)

        #  Do some 'work'
        time.sleep(1)

        #  Send reply back to client
        socket.send(b"World")


def _recv_config_send_Xy():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        #  Wait for next request from client
        message = socket.recv_json()
        print("Received request: {}".format(message))
        dataset = generate_batch_Xy(message['eq_name'], message['batch_size'])

        #  Do some 'work'
        time.sleep(1)
        print('Sending data pairs: {}'.format(dataset.shape))
        #  Send reply back to client
        socket.send(dataset)


def generate_batch_Xy(dataset_name, sample_size):
    print(f'Generating dataset `{dataset_name}` ...')
    print()
    dataset_kwargs = dict()

    # Instantiate equation object
    sampling_objs = build_sampling_objs(dataset_kwargs.pop('sampling_objs')) if 'sampling_objs' in dataset_kwargs else None
    eq_instance = get_eq_obj(dataset_name, sampling_objs=sampling_objs, **dataset_kwargs)
    # Generate tabular dataset
    dataset = eq_instance.create_dataset(sample_size)
    return dataset


def generate_cvgp_format_dataset(dataset_name, sample_file_size, singlefile_sample_size=256):
    print(f'Generating dataset `{dataset_name}` ...')
    dataset_kwargs = dict()
    # Instantiate equation object
    sampling_objs = build_sampling_objs(dataset_kwargs.pop('sampling_objs')) if 'sampling_objs' in dataset_kwargs else None
    eq_instance = get_eq_obj(dataset_name, sampling_objs=sampling_objs, **dataset_kwargs)

    # Write out each split
    fixed_column = [i for i in range(len(eq_instance.x))]
    dataset = eq_instance.create_fixedcolumn_dataset(singlefile_sample_size, fixed_column)
    return dataset





if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Dataset generator')
    # parser.add_argument('--config', required=True, help='config file path')
    #
    # main(parser.parse_args())
    _recv_config_send_Xy()
