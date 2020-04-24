from rest_framework import serializers
from .models import Todo,Schedule

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = ('id', 'title', 'description', 'completed')

class ScheduleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Schedule
		fields = ('id', 'title','time' ,'location','description','completed')