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

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance

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