from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import DetailView

TODOS = [
    {
        'todo_id': 1,
        'title': 'todo 1',
        'text': 'какое-то задание',
        'block': 'block1'
    },
    {
        'todo_id': 2,
        'title': 'todo 2',
        'text': 'какое-то задание',
        'block': 'block2'
    },
    {
        'todo_id': 3,
        'title': 'todo 3',
        'text': 'какое-то задание',
        'block': 'block3'
    },
]

menu = [
    {'title':'Главная страница', 'url_name': 'todos'},
    {'title':'О сайте', 'url_name': 'about'},
    {'title':'Обратная связь', 'url_name':'contact'},
    {'title':'Войти','url_name':'login'},
]


def todos(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'title': 'Главная страница',
        'menu': menu}
    return render(request, 'todos.html', context=context)


def get_todo(request, todo_id):
    global TODOS
    todo = next((todo for todo in TODOS if todo['todo_id'] == todo_id), None)
    if todo:
        if request.method == 'GET':
            return render(request, 'todo.html', {'title': 'Дело', 'todos': todo})
        elif request.method == 'DELETE':
            TODOS = [todo for todo in TODOS if todo['todo_id'] != todo_id]
            return HttpResponse(status=200)
    return HttpResponse(status=404)

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo.html'
    context_object_name = 'one_todo'



def create(request):
    error = ''
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
        else:
            error = 'Неверные данные, поля должны быть заполнены.'

    form = TodoForm()
    context = {
        'form': form,
        'title': 'Добавление задачи',
        'menu': menu,
        'error': error}
    return render(request, 'create.html', context=context)


def about(request):
    return render (request, 'about.html', {'menu': menu, 'title': 'О сайте'})


def contact(request):
    return render (request, 'contact.html', {'menu': menu, 'title': 'Обратная связь'})


def login(request):
    return render(request, 'login.html', {'menu': menu, 'title': 'Войти'})




