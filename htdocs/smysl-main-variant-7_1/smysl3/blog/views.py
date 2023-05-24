from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Item, Profile, Additional, Comment
from .forms import UserRegisterForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home_page(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'home_page.html', context)


def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'article_page.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    comment = Comment.objects.all()
    context = {'comment': comment}
    return render(request, 'profile.html', context)


def additional_content(request):
    additional = Additional.objects.get()
    context = {'additional': additional}
    return render(request, 'additional_content.html', context)


def comment(request):
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CommentForm(data=request.POST)

    return render(request, 'comment.html', {'form': form})

