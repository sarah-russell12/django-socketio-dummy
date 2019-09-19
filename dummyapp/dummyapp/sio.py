# -*- coding: utf-8 -*-
"""
sio.py

Created on Tue Sep 17 13:01:26 2019

@author: Sarah
"""

import socketio
from .wsgi import application

server = socketio.Server()

@server.event
def double(sid, data):
    number = int(data.number)
    number *= 2
    server.emit('double response', {'result' : number}, room=sid)
    
sioApp = socketio.WSGIApp(server, application)
