from django.contrib import admin
from .models import Todo

admin.site.register(Todo)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'comment')