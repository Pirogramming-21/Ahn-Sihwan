from django.urls import path
from .views import *

app_name='movielog'

urlpatterns = [
    path('review/', review_list),
    path('review/<int:pk>/', review_detail),
    path('review/create/', review_create),
    path('review/<int:pk>/update/', review_update),
]