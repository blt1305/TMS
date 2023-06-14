from . import views
from django.urls import path

urlpatterns = [
    path('', views.todos, name="todos"),
    path('home/', views.home_todos)
]