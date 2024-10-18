from django.shortcuts import render
from rest_framework import viewsets
from modules.tasks.models import Task, TaskStatus
from modules.tasks.api.v1.serializers import TaskSerializer, TaskStatusSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskStatusViewSet(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer