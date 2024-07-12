from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def review_list(request):
    sort_by = request.GET.get('sort_by', 'title')  # URL 쿼리 매개변수 'sort_by'를 가져옴. 기본값은 제목
    order = request.GET.get('order', 'asc') # 정렬 방향 설정. 기본값은 오름차순
    if order == 'desc':
        sort_by = f'-{sort_by}' # 내림차순이면 순서 뒤집기
    reviews=Review.objects.all().order_by(sort_by) # 정렬 기준에 따라 reviews 가져와서 정렬
    context={
        'reviews':reviews,
        'sort_by':sort_by,
        'order': order
    }
    return render(request, 'review_list.html', context)

def review_detail(request, pk):
    review=Review.objects.get(id=pk)
    context={
        "review":review
    }
    # (챌린지) 리뷰 러닝타임 변환
    review.running_time_hours = review.running_time // 60 #시간
    review.running_time_minutes = review.running_time % 60 #분
    return render(request, 'review_detail.html', context)

def review_create(request):
    if request.method=="POST":
        form=ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review=form.save()
            return redirect(f'/review/')
    else:
        form=ReviewForm()
    return render(request, 'review_create.html', {'form': form})

def review_update(request, pk):
    review=Review.objects.get(id=pk)
    if request.method=="POST":
        form=ReviewForm(request.POST, request.FILES, instance=review) #instace=review는 수정용, Django에서 제공
        if form.is_valid():
            review=form.save()
            return redirect(f'/review/{review.pk}/')
    else:
        form=ReviewForm(instance=review)
    return render(request, 'review_create.html', {'form': form})

def review_delete(request, pk):
    if request.method=="POST":
        review=Review.objects.get(id=pk)
        review.delete()
    return redirect('/review/')