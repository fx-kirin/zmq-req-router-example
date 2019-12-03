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
import zmq


def start_client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")

    while True:
        print("Enter message:")
        message = sys.stdin.readline()
        socket.send_string(message.strip())

        recv_message = socket.recv_string()
        print("Receive message = %s" % recv_message)

    socket.close()
    context.destroy()


if __name__ == "__main__":
    start_client()
