from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def pagina(request):
    return render(request, 'blog/pagina.html', {})

def direccion (request):
    return render(request, 'blog/direccion.html', {})