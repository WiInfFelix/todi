from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo

from .serializers import TodoSerializer
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
