from django.urls import path
from Teacher.views import *

urlpatterns = [
    path('login/', login),
    path('register/',register),
    path('index/',index),
    path('info/',info),
    path('changePassword/',changePassword),
]
