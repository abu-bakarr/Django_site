from django.shortcuts import render
import request
from django.http import HttpResponse
from .models import Post
from bs4 import BeautifulSoup

posts = Post.objects.all()[:10]
context = {
    'title': 'My First Django Blog',
    'id': 123,
    'posts': posts,
    'name': 'Lovel Bangura'
}

# Create your views here.


def index(request):
    return render(request, 'polls/index.html', context)


def details(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'poll/details.html', context)

    context = {
        'post': post
    }


def new_search(request):
    searchData = ''
    searchData = request.POST.get('search')
    if searchData == "None":
        searchData = ""
    else:
        context = {
            'searchData': searchData,

        }
    print(searchData)
    return render(request, 'polls/new_search.html', context)
