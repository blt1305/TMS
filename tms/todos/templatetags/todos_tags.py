from django import template
from todos.models import *


register = template.Library()

@register.simple_tag()
def get_menu():
    '''возвращает контекстное меню'''
    menu = [
        {'title':'Главная страница', 'url_name': 'todos'},
        {'title':'О сайте', 'url_name': 'about'},
        {'title':'Обратная связь', 'url_name':'contact'},
        {'title':'Войти','url_name':'login'},
    ]
    return menu