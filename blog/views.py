from django.shortcuts import render
from .models import Blogpost
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    myposts= Blogpost.objects.all()
    return render(request, 'blog/index.html', {'myposts': myposts})


def blogspot(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request, "blog/blogspot.html", {'post': post})
