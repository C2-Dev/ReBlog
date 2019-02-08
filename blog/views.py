from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import PostForm, ProfileForm
from .models import Post
from datetime import date, timedelta
from django.utils import timezone

def tab1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                entry = form.save(commit=False)
                entry.author = request.user
                entry.save()
                return redirect('tab2')
            else:
                print(form.errors)
        else:
            form = PostForm()
            return render(request, 'blog/tab1.html', {'form': form})
    else:
        return redirect('login')

def tab2(request):
    if request.user.is_authenticated:
        top_posts = Post.objects.all()
        return render(request, 'blog/tab2.html', {'top_posts': top_posts})
    else:
        return redirect('login')

def tab3(request):
    if request.user.is_authenticated:
        return render(request, 'blog/tab3.html')
    else:
        return redirect('login')
