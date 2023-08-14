from . import views
from django.urls import path

urlpatterns = [
    path('', views.todos, name="todos"),
    path('todo/<int:id>/', views.TodoDetail.as_view(), name="one_todo"),
    path('review/<int:id>/', views.AddComment.as_view(), name="add_comment"),
    path('<int:id>/add_likes/', views.AddLike.as_view(), name='add_likes'),
    path('<int:id>/del_likes/', views.DelLike.as_view(), name='del_likes'),
    path('todo/<int:pk>/update', views.TodoUpdateView.as_view(), name="todo_update"),
    path('todo/<int:pk>/delete', views.TodoDeleteView.as_view(), name="todo_delete"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('create/', views.create, name="create"),
]


