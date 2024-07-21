from django.urls import path
from .views import *

app_name = 'pirostagram'

urlpatterns = [
    path('', base, name='base'),
]