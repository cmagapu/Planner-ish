from django.contrib import admin
from .models import Todo,Schedule

class TodoAdmin(admin.ModelAdmin):
	list_display = ('title','description','completed')

class ScheduleAdmin(admin.ModelAdmin):
	list_display = ('title','time','location','description')

admin.site.register(Todo,TodoAdmin)
admin.site.register(Schedule,ScheduleAdmin)