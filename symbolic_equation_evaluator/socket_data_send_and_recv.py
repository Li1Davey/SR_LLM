import time

import zmq
import numpy as np


def _send_config_recv_Xy(batch_size=256):
    idx = 0
    context = zmq.Context()

    #  Socket to talk to server
    print("Connecting to hello world server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    #  Do 10 requests, waiting each time for a response
    st = time.time()
    for request in range(10 ** 6):
        # print("Sending request %s …" % request)
        config = {'batch_size': batch_size,
                  'dataset_name': 'symbolic_equation_evaluator-easy',
                  'eq_name': 'FeynmanIICh15Eq5'}

        socket.send_json(config)

        #  Get the reply.
        message = socket.recv()
        data_xy = np.frombuffer(message, dtype=float).reshape(batch_size, -1)
        # print("Received reply {}".format(data_xy.shape))
        idx += 1
        if idx % 100 == 0:
            print("received", idx)
    print("time used:", time.time() - st)


# def gen_np_rand(batch_size=10, nvar=3):
#     return np.random.randn(batch_size, nvar)


if __name__ == '__main__':
    _send_config_recv_Xy()
