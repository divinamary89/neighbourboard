from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home_view(request):
    category = request.GET.get('category', '')
    if category:
        posts = Post.objects.filter(category=category).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts, 'selected': category})

@login_required(login_url='login')
def create_post_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        Post.objects.create(
            title=title,
            content=content,
            category=category,
            author=request.user,
            contact=request.POST['contact']
        )
        return redirect('home')
    return render(request, 'create_post.html')
@login_required(login_url='login')
def profile_view(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'profile.html', {'posts': posts})