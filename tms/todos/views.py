from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

TODOS = [
    {
        'title': 'todo 1',
        'text': 'какое-то задание'
    },
    {
        'title': 'todo 2',
        'text': 'какое-то задание'
    },
    {
        'title': 'todo 3',
        'text': 'какое-то задание'
    },
]
def home_todos(request):
    return render(request, 'todos.html', {'title': 'Список дел', 'todos': TODOS})

def todos(request):
    return JsonResponse({'todos': TODOS})