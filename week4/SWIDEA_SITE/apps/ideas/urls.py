from django.urls import path
from .views import *

app_name = 'ideas'

urlpatterns = [
    path('', main, name='main'),
    path('register/', register, name='register'),
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/delete/', delete, name='delete'),
    path('<int:pk>/update/', update, name='update'),
    path('<int:pk>/bookmark/', bookmark, name='bookmark'),
]