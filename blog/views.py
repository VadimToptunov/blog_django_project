from django.shortcuts import render
from datetime import date
posts = [
    {
        'author': 'VT',
        'title': 'First Blog Post',
        'content': 'First post content',
        'date_posted': str(date.today())
    },
{
        'author': 'SvS',
        'title': 'Second Blog Post',
        'content': 'Second post content',
        'date_posted': str(date.today())
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
