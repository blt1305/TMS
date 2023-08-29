import io

from .models  import Todo
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# class TodoModel:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description


class TodoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    created_date = serializers.DateField(read_only=True)
    author_id = serializers.IntegerField()
    completed = serializers.BooleanField(default=False)

# def encode():
#     model = TodoModel('домашняя работа', 'уборка')
#     model_sr = TodoSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream =io.BytesIO(b'{"title":"домашняя работа", "description":"уборка"}')
#     data = JSONParser().parse(stream)
#     serializers = TodoSerializer(data = data)
#     serializers.is_valid()
#     print(serializers.validated_data)


# class Meta:
#     model = Todo
#     fields = ['id', 'title', 'description', 'created_date', 'author']