from .models  import Todo
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

class TodoModel:
    def __init__(self, title, description):
        self.title = title
        self.description = description


class TodoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()

def encode():
    model = TodoModel('домашняя работа', 'уборка')
    model_sr = TodoSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


# class Meta:
#     model = Todo
#     fields = ['id', 'title', 'description', 'created_date', 'author']