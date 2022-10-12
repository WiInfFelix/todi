from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        read_only_fields = ("id", "created_at", "creator")
        fields = "__all__"
