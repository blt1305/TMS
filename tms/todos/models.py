from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=120, default='')
    description = models.TextField(default='')
    created_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50, default='')
