# -*- coding: utf-8 -*-
"""
sio.py

Created on Tue Sep 17 13:01:26 2019

@author: Sarah
"""

import socketio

server = socketio.Server()

@server.event
def double(sid, data):
    number = int(data.number)
    number *= 2
    server.emit('multiply response', {'result' : number})