from django import forms
from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, NullBooleanSelect, Textarea


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'created_date', 'author', 'completed']

        widgets = {
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Название задачи'
            }),
            'description': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Содержание задачи'
            }),
            'created_date': DateTimeInput(attrs={
                'class': "form-control",
                'placeholder': 'Дата публикации'
            }),
            'author': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Автор'
            }),
            'completed': NullBooleanSelect(attrs={
                'class': "form-control",
                'placeholder': 'Выполнено'
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email_address', 'comment_text')