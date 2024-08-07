from django.urls import path
from .views import *

app_name = 'devtools'

urlpatterns = [
    path('', main, name='main'),
    path('register/', register, name='register'),
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/delete/', delete, name='delete'),
    path('<int:pk>/update/', update, name='update'),
]