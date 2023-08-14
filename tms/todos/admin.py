from django.contrib import admin
from .models import *

admin.site.register(Todo)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment')


admin.site.register(Comment, CommentAdmin)