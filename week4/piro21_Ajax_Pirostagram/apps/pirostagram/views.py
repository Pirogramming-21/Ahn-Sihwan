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

@login_required
def leave_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        text = request.POST.get('text')
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(post=post, user=request.user, text=text)
        return JsonResponse({'id': comment.id, 'user': comment.user.username, 'text': comment.text})

@login_required
def delete_comment(request):
    comment_id = request.POST.get('comment_id')
    comment = Comment.objects.get(id=comment_id)
    if comment.user == request.user:
        comment.delete()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'}, status=403)