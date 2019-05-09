from django.shortcuts import render, redirect
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
# Create your views here.

def home(request):
    reviews = Review.objects.all()
    return render(request, 'home.html', { 'reviews' : reviews })


def new(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        review = form.save(commit=False)
        form.save()
        return redirect('detail', review.pk)
    else:
        form = ReviewForm()
    return render (request, 'new.html', {'form' : form})


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.review = review
        comment.save()

        return redirect('detail', review.pk)
    else:
        form = CommentForm()

        return render(request, 'detail.html', { 'review' : review, 'form' : form })


def edit(request, review_pk):
    review = Review.objects.get(pk = review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance = review)
        form.save()
        return redirect('detail', review.pk)
    else:
        form = ReviewForm(instance = review)
        return render(request,'edit.html', { 'form' : form })

def delete(request, review_pk):
    review = Review.objects.get(pk = review_pk)
    review.delete()
    return redirect('home')


def delete_comment(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    comment.delete()
    return redirect('detail', review_pk)