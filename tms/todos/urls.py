from . import views
from django.urls import path

urlpatterns = [
    path('', views.todos, name="todos"),
    path('home/', views.home_todos),
    path('home/<int:todo_id>/', views.get_todo),
    path('addtask/', views.add_task)
]