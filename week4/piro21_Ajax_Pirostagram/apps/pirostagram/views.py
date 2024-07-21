from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
import json

# Create your views here.
def posts(request):
  posts = Post.objects.all()
  ctx = {
    'posts': posts
  }
  return render(request, 'pirostagram/list.html', ctx)


# @csrf_exempt #csrf 토근 검사 해제
# def like_post(request):
#   req = json.loads(request.body)
#   post_id = req['id']
#   button_type = req['type']

#   post = Post.objects.get(id=post_id)

#   if button_type == 'like':
#     post.likes += 1
#   else:
#     post.likes -= 1

#   post.save()

#   return JsonResponse({'id': post_id, 'type': button_type})

@login_required
def like_post(request):
  post_id = request.POST.get('id')
  button_type = request.POST.get('type')

  post = Post.objects.get(id=post_id)

  if button_type == 'like':
      if request.user not in post.likes.all():
          post.likes.add(request.user)
  else:
      if request.user in post.likes.all():
          post.likes.remove(request.user)

  return JsonResponse({'id': post.id, 'type': button_type, 'likes': post.likes.count()})
