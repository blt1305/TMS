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
    if request.method == 'GET':
        return JsonResponse({'todos': TODOS})
    elif request.method == 'POST':
        todo = dict(request.POST)
        todo['todo_id'] = int(todo['todo_id'][0])
        todo['title'] = todo['title'][0]
        todo['text'] = todo['text'][0]
        TODOS.append(todo)
        return JsonResponse({'todos': todo})


def get_todo(request, todo_id):
    global TODOS
    todo = next((todo for todo in TODOS if todo['todo_id'] == todo_id), None)
    if todo:
        if request.method == 'GET':
            return JsonResponse({'todos': todo})
        elif request.method == 'DELETE':
            TODOS = [todo for todo in TODOS if todo['todo_id'] != todo_id]
            return HttpResponse(status=200)
    return HttpResponse(status=404)

