from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    name = models.CharField(max_length=120, default='')
    description = models.TextField(default='')
    created_date = models.DateField(default=date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/todo/{self.id}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'