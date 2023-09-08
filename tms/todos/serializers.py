from .models  import Todo
from rest_framework import serializers



class TodoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Todo
        fields = '__all__'