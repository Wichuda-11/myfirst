from django.shortcuts import render
from .serializers import TaskSerializer
from rest_framework import generics, permissions
from .models import Task

# class Based Views
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Retrieve=GET (detail)
# Update=PUT
# Destroy=DELETE
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
