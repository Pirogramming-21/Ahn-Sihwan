from django.shortcuts import render, redirect
from .models import Devtool
from .forms import DevtoolForm

def main(req):
    devtools = Devtool.objects.all()
    ctx = {'devtools':devtools}
    return render(req, 'devtools/list.html', ctx)

def register(req):
    if req.method == 'GET':
        form = DevtoolForm()
        ctx = {'form': form}
        return render(req, 'devtools/register.html', ctx)
    form = DevtoolForm(req.POST, req.FILES)
    if form.is_valid():
        form.save()
    return redirect('devtools:main')

def detail(req,pk):
    devtool = Devtool.objects.get(id=pk)
    ctx = {'devtool': devtool}
    return render(req, 'devtools/detail.html', ctx)

def delete(req,pk):
    if req.method == 'POST':
        Devtool.objects.get(id=pk).delete()
    return redirect('devtools:main')

def update(req, pk):
    devtool = Devtool.objects.get(id=pk)
    if req.method == 'GET':
        form = DevtoolForm(instance=devtool)
        ctx = {'form': form, 'pk': pk}
        return render(req, 'devtools/update.html', ctx)
    form = DevtoolForm(req.POST, req.FILES, instance=devtool)
    if form.is_valid():
        form.save()
    return redirect('devtools:main')