from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post


def home(request):
	return render(request, 'index.html')

def posts(request):
	posts = Post.objects.all()
	return render(request, 'posts.html',{'posts':posts})

def about(request):
	return render(request, 'about.html')
