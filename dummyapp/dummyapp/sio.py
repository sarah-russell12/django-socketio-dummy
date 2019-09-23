# -*- coding: utf-8 -*-
"""
sio.py

Created on Tue Sep 17 13:01:26 2019

@author: Sarah
"""

from socketio import Server, WSGIApp
from .wsgi import application

server = Server()

@server.event
def double(sid, data):
    number = int(data.number)
    number *= 2
    server.emit('double response', {'result' : number}, room=sid)
    
sioApp = WSGIApp(server, application)
