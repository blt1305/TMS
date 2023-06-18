from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

TODOS = [
    {
        'todo_id': 1,
        'title': 'todo 1',
        'text': 'какое-то задание'
    },
    {
        'todo_id': 2,
        'title': 'todo 2',
        'text': 'какое-то задание'
    },
    {
        'todo_id': 3,
        'title': 'todo 3',
        'text': 'какое-то задание'
    },
]
def todos(request):
    return render(request, 'todos.html', {'title': 'Список дел', 'todos': TODOS})

def home_todos(request):
    return JsonResponse({'todos': TODOS})

def get_todo(request, todo_id):
    todo = next((todo for todo in TODOS if todo['todo_id'] == todo_id), None)
    if todo:
        return JsonResponse({'todo': todo})
    return HttpResponse(status=404)