from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.generic.base import View
from .forms import CommentForm


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


class TodoDetail(View):
    '''отдельная запись'''
    def get(self, request, id):
        one_todo = Todo.objects.get(id=id)
        return render(request, 'todo.html', {'one_todo': one_todo, 'title': one_todo.title, 'menu': menu})


class AddComment(View):
    # def post(self, request, id):
    #     form = CommentForm(request.POST)
    #
    #     if form.is_valid():
    #         form = form.save(commit=False)
    #         form.id = id
    #         form.save()
    #     return redirect('/')

    def post(self, request, id):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.comment_id = id
                form.save()

        return redirect(f'/todo/{id}')


class TodoUpdateView(UpdateView):
    '''обновление задачи'''
    model = Todo
    template_name = 'create.html'
    form_class = TodoForm


class TodoDeleteView(DeleteView):
    '''удаление задачи'''
    model = Todo
    success_url = '/'
    template_name = 'todo_delete.html'
    context_object_name = 'todo_delete'


def create(request):
    '''добавление задачи'''
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




