# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:34:34 2019

@author: Sarah
"""

from django.urls import path

from . import views

urlpatterns = [
        path('home/', views.home, name='home'),
        path('play-with-sockets/', views.play, name='play'),
        ]
