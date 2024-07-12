from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def review_list(request):
    reviews=Review.objects.all()
    context={
        'reviews':reviews
    }
    return render(request, 'review_list.html', context)

def review_detail(request, pk):
    review=Review.objects.get(id=pk)
    context={
        "review":review
    }
    return render(request, 'review_detail.html', context)

def review_create(request):
    if request.method=="POST":
        form=ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review=form.save()
            return redirect(f'/review/{review.pk}/')
    else:
        form=ReviewForm()
    return render(request, 'review_create.html', {'form': form})