from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.generic.base import View
from .forms import CommentForm
from rest_framework import generics
from .serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

def todos(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'title': 'Главная страница'}
    return render(request, 'todos.html', context=context)


class TodoDetail(View):
    '''отдельная запись'''
    def get(self, request, id):
        one_todo = Todo.objects.get(id=id)
        return render(request, 'todo.html', {'one_todo': one_todo, 'title': one_todo.title})


class AddComment(View):
    def post(self, request, id):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.comment_id = id
                form.save()
        return redirect(f'/todo/{id}')



def get_client_ip(request):
    '''получаем ip-адрес клиента'''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    '''добавление лайков'''
    def get(self, request, id):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip = ip_client, post_id = id)
            return redirect(f'/todo/{id}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.post_id = int(id)
            new_like.save()
            return redirect(f'/todo/{id}')


class DelLike(View):
    '''удаление лайков'''
    def get(self, request, id):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip = ip_client, post_id = id).delete()
            return redirect(f'/todo/{id}')
        except:
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
        'error': error}
    return render(request, 'create.html', context=context)


def about(request):
    return render (request, 'about.html', { 'title': 'О сайте'})


def contact(request):
    return render (request, 'contact.html', { 'title': 'Обратная связь'})


def login(request):
    return render(request, 'login.html', { 'title': 'Войти'})

#_______________________________________________________#

# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     permission_classes = [permissions.AllowAny]
#     filter_backends = [filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter]
#     ordering_fields = ['id', 'title', 'description', 'created_date']
#     filterset_fields = ['id', 'title', 'description', 'author']
#     search_fields = ['title', 'description']

class TodoAPIList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoAPIUpdate(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# class TodoAPIView(APIView):
#     def get(self, request):
#         td= Todo.objects.all()
#         return Response({'todos': TodoSerializer(td, many=True).data})         #получаем js, м-д GET
#
#     def post(self, request):                                                    #метод POST, создание записи
#         serializer = TodoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'todo': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if  not pk:
#             return Response({'error':'Метод PUT не определен'})
#
#         try:
#             instance = Todo.objects.get(pk = pk)
#         except:
#             return Response({'error':'Метод PUT не определен'})
#
#         serializer = TodoSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'todo': serializer.data})
#
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if  not pk:
#             return Response({'error':'Метод DELETE не определен'})
#
#         try:
#             instance = Todo.objects.get(pk = pk)
#             instance.delete()
#         except:
#             return Response({'error':'Метод PUT не определен'})
#
#         return Response({'todo': 'delete todo' + str(pk)})
