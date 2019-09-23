"""
a LOT of this is based on the code from the django-socketio example inside the python-socketio github repo

https://github.com/miguelgrinberg/python-socketio/

"""

from django.shortcuts import render
from django.template import loader
from django.views import generic

import os
import socketio

basedir = os.path.dirname(os.path.realpath(__file__))
server = socketio.Server(async_mode='eventlet')
thread = None

# Create your views here.
def home(request):
    global thread
    if thread is None:
        thread = server.start_background_task(background_thread)
    return render(request, 'double/home.html')

def background_thread():
    count = 0
    while True:
        server.sleep(10)
        count += 1
        server.emit('connected', {'data' : 'You are still connected'})

@server.event
def double(sid, message):
    number = int(message['number'])
    number *= 2
    server.emit('double_response', {'data' : number}, room=sid)

@server.event
def connect(sid, environ):
    print("Client with sid {sid} connected".format(sid=sid))
    server.emit('connected', {'data' : 'You are connected'})

@server.event
def disconnect(sid):
    print("Client with sid {sid} disconnected".format(sid=sid))

