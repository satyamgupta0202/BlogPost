from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(response):
    context={
      'posts': posts
    }
    return render(response ,'blog/home.html',context)

def about(response):
    return render(response ,'blog/about.html',{'title':'about'})
