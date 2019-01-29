from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import PostForm, ProfileForm
from datetime import date, timedelta
from django.utils import timezone

def index(request):
    if request.user.is_authenticated:
        return render(request, 'blog/index.html')
    else:
        return redirect('login')


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                post = form.save(commit=False)
                post.created_on = timezone.now()
                post.author = request.user
                post.save()
                return redirect('..')
            else:
                return redirect('login')
    else:
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'blog/profile.html')
    else:
        return redirect('login')


def update_profile(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'blog/update_profile.html', {
        'profile_form': profile_form
    })