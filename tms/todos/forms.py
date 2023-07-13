from django import forms
from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, NullBooleanSelect, Textarea


# class AddTaskForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     text = forms.CharField(max_length=255)
#     block = forms.CharField(max_length=255)


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'description', 'created_date', 'author', 'completed']

        widgets = {
            "name": TextInput(attrs={
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

