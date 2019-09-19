# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:34:34 2019

@author: Sarah
"""

from django.urls import path

from .views import HomeView

urlpatterns = [
        path('home/', HomeView.as_view(), name='home'),
        ]