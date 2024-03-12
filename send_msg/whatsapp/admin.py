from django.contrib import admin
from .models import Representative, Team, Status, Tournament

@admin.register(Representative)
class RepresentativeAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('town', 'data')
    list_filter = ('status',)
    

""" 
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('regions', 'timezone', 'ordering', 'publication')
    list_filter = ('regions', 'publication')
    list_editable = ('ordering',) """