from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo, Schedule
from .serializers import TodoSerializer,ScheduleSerializer

class TodoView(viewsets.ModelViewSet):
	serializer_class = TodoSerializer
	queryset = Todo.objects.all()

class ScheduleView(viewsets.ModelViewSet):
	serializer_class = ScheduleSerializer
	queryset = Schedule.objects.all()
