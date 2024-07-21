from django.urls import path
from .views import *

app_name = 'pirostagram'  # URL 네임스페이스 추가

urlpatterns = [
    path('', posts, name='posts'),
    path('like/', like_post, name='like_post'),
    # path('comment/', comment_post, name='comment_post'),
    # path('delete_comment/', delete_comment, name='delete_comment'),
]