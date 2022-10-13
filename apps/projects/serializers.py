from rest_framework import serializers

from apps.todos.serializers import TodoSerializer

from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    members = None
    todos = TodoSerializer(many=True)

    class Meta:
        model = Project
        fields = ("name", "members", "todos")
        