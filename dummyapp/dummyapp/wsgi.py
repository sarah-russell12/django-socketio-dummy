"""
WSGI config for dummyapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from socketio import WSGIApp

from double.views import server

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dummyapp.settings')

application = get_wsgi_application()

application = WSGIApp(server, application)
import eventlet
eventlet.wsgi.server(eventlet.listen(('', 8000)), application)
