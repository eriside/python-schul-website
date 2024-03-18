from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def betriebssysteme(request):
    
    return render(request, 'betriebssysteme.html')

def bootstrap(request):
    
    return render(request, 'bootstrap.html')

def impressum(request):
    
    return render(request, 'impressum.html')

def lernplan(request):
    
    return render(request, 'lernplan.html')

def linksammlung(request):
    
    return render(request, 'linksammlung.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/home')


def dashboard(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'aktuelles.html', {'posts': posts})

@staff_member_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)  # Stelle sicher, dass du request.FILES übergibst, um das Bild zu akzeptieren
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})

@staff_member_required
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

@staff_member_required
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Der Blog-Beitrag wurde erfolgreich gelöscht.')
        return redirect('admin_dashboard')
    return render(request, 'delete_post.html', {'post': post})

@staff_member_required
def admin_dashboard(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'admin_dashboard.html', {'posts': posts})