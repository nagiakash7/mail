from django.urls import path
from .views import *

app_name='app'

urlpatterns=[
    path('',email_sending_func,name='email-send')
]