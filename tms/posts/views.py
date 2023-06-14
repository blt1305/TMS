from django.http import JsonResponse
from django.shortcuts import render


POSTS = [
    {
        'title': 'post 1',
        'text': 'какой-то текст поста'
    },
    {
        'title': 'post 2',
        'text': 'какой-то текст поста'
    },
    {
        'title': 'post 3',
        'text': 'какой-то текст поста'
    },
]


def home(request):
    return render(request, 'home.html', {'posts': POSTS})


def posts(request):
    return JsonResponse({'posts': POSTS})