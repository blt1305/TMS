from django.contrib.auth.models import User

from .models import Todo


def create_initial_db():
    name_lst = ['Harry', 'Ron', 'Hermione']
    for n in name_lst:
        user = User.objects.create_user(
            username = n,
            email = n + '@gmail.com',
            password = '12345'
        )
        # print(user.username)

        todo = Todo.objects.create( name = 'не знаю как достать имя', description ='the task', author = User.objects.get(username = n))
        todo.save()


