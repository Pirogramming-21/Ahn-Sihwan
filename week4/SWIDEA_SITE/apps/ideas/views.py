from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm

def main(req):
    ideas = Idea.objects.all()
    ctx = {'ideas':ideas}
    return render(req, 'ideas/list.html', ctx)

def register(req):
    if req.method == 'GET':
        form = IdeaForm()
        ctx = {'form': form}
        return render(req, 'ideas/register.html', ctx)
    form = IdeaForm(req.POST, req.FILES)
    if form.is_valid():
        form.save()
    return redirect('ideas:main')