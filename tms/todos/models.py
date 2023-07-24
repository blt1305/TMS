from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    '''задания
    поля: название задачи, описание, дата создания, автор, выполнена/не выполнена'''
    title = models.CharField(max_length=120, default='')
    description = models.TextField(default='')
    created_date = models.DateField(default=date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/todo/{self.id}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


# class Comment(models.Model):
#     '''комментарии под записью'''
#     email_address = models.EmailField(default='')
#     name = models.CharField(max_length=255, verbose_name='Имя пользователя')
#     comment_text = models.TextField(max_length=2000, verbose_name='Текст комментария')
#     comment = models.ForeignKey(Todo, on_delete=models.CASCADE, verbose_name='Задача')
#
#     def __str__(self):
#         return self.name, self.comment
#
#     class Meta:
#         verbose_name = 'Комментарий'
#         verbose_name_plural  = 'Комментарии'
