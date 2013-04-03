from django.contrib import admin
from hightail.sprint.models import Sprint, SprintProject, SprintCard, Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']
    list_per_page = 25

class SprintAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'start_date', 'end_date', 'status', 'author_id')
    list_filter = ['status', 'pub_date', 'start_date', 'end_date']
    search_fields = ['author_id', 'description', 'notes']
    list_per_page = 25
    
class SprintProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'start_date', 'end_date', 'status', 'author_id')
    list_filter = ['status', 'pub_date', 'start_date', 'end_date']
    search_fields = ['author_id', 'description', 'notes']
    list_per_page = 25
    
class SprintCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'points', 'pub_date', 'start_date', 'end_date', 'status', 'author_id')
    list_filter = ['status', 'pub_date', 'start_date', 'end_date']
    search_fields = ['author_id', 'content', 'notes']
    list_per_page = 25