from . import views
from django.urls import path

urlpatterns = [
    path('', views.todos, name="todos"),
    path('todo/<int:pk>/', views.TodoDetailView.as_view(), name="one_todo"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('create/', views.create, name="create"),
]