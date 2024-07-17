from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Idea
from .forms import IdeaForm

def main(req):
    sort_by = req.GET.get('sort_by', 'title')  # URL 쿼리 매개변수 'sort_by'를 가져옴. 기본값은 제목
    order = req.GET.get('order', 'asc')
    if order == 'desc':
        sort_by = f'-{sort_by}' # 내림차순이면 순서 뒤집기
    ideas = Idea.objects.all().order_by(sort_by)
    paginator = Paginator(ideas, 4)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    ctx = {
        'ideas':ideas,
        'order': order,
        'sort_by': sort_by,
        'page_obj': page_obj
        }
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

def bookmark(req, pk):
    idea = Idea.objects.get(id=pk)
    idea.bookmark = not idea.bookmark
    idea.save()
    return redirect('ideas:main')