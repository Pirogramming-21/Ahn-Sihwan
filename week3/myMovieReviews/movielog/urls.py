from django.urls import path
from .views import *

app_name='movielog'

urlpatterns = [
    path('review/', review_list),
]