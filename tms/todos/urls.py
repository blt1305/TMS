from . import views
from django.urls import path

urlpatterns = [
    path('', views.todos, name="todos"),
    path('todo/', views.home_todos, name = 'home_todos'),
    path('todo/<int:todo_id>/', views.get_todo, name="todo"),
    path('addtask/', views.add_task, name="add_task"),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('login/', views.login, name = 'login'),
    path('create/', views.create, name="create"),
]