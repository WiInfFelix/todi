from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)

    class Meta:
        model = Todo
        read_only_fields = ("id", "created_at", "creator")
        fields = "__all__"
