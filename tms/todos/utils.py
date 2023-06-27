from models import Todo

Todo.objects.all()                                      #получение всех записей (будет отобразаться только name,
                                                        # т.к. в модели в м-де __str__ определено return self.name

Todo.objects.all().values('id', 'author')               #id и name для всех записей в виде списка словарей
[(i.id, i.name) for i in Todo.objects.all()]            #id и name для всех записей в виде списка кортежей

Todo.objects.get(id=3).description                      #получение поста по id

[i.description for i in Todo.objects.all()]             #содержание всех постов в виде списка

Todo.objects.get(name__contains='gu').description        #получение содержания поста по части названия