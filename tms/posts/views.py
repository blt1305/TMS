from django.http import JsonResponse
from django.shortcuts import render


POSTS = [
    {
        'posts_id': 1,
        'title': 'post 1',
        'text': 'какой-то текст поста',
        'block': 'block1'
    },
    {
        'posts_id': 2,
        'title': 'post 2',
        'text': 'какой-то текст поста',
        'block': 'block2'
    },
    {
        'posts_id': 3,
        'title': 'post 3',
        'text': 'какой-то текст поста',
        'block': 'block3'
    },
]


def home(request):
    return render(request, 'home.html', {'title': 'Список постов', 'posts': POSTS})

def posts(request):
    return JsonResponse({'posts': POSTS})