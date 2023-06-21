from django import forms
from .models import *


class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(max_length=255)
    block = forms.CharField(max_length=255)



