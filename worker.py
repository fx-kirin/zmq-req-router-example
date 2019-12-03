#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 fx-kirin <fx.kirin@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import sys
import time

import zmq


def start_worker(worker_name):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect("tcp://localhost:5557")

    print("Start worker: %s" % worker_name)

    while True:
        message = socket.recv_string()
        print("Receive message = %s" % message)
        print("Sleep5")
        time.sleep(5)
        print("Sleep5 finished")

        reply_message = "Reply %s from %s" % (message, worker_name)

        socket.send_string(reply_message)

    socket.close()
    context.destroy()


if __name__ == "__main__":
    start_worker(sys.argv[1])
