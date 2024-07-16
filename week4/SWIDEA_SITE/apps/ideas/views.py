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

def detail(req,pk):
    idea = Idea.objects.get(id=pk)
    ctx = {'idea': idea}
    return render(req, 'ideas/detail.html', ctx)

def delete(req,pk):
    if req.method == 'POST':
        Idea.objects.get(id=pk).delete()
    return redirect('ideas:main')

def update(req, pk):
    idea = Idea.objects.get(id=pk)
    if req.method == 'GET':
        form = IdeaForm(instance=idea)
        ctx = {'form': form, 'pk': pk}
        return render(req, 'ideas/update.html', ctx)
    form = IdeaForm(req.POST, req.FILES, instance=idea)
    if form.is_valid():
        form.save()
    return redirect('ideas:main')