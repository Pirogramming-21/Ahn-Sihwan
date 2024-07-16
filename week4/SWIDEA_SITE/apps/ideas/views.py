from django.shortcuts import render, redirect

def main(req):
    return render(req, 'ideas/list.html')