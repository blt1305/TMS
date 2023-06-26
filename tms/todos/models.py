from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    name = models.CharField(max_length=120, default='')
    description = models.TextField(default='', help_text='Напишите что-нибудь')
    created_date = models.DateField(default=date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name