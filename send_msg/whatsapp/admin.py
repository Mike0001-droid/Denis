from django.contrib import admin
from .models import Contact, Rodkom, Trener, Team

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Rodkom)
class RodkomPlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Trener)
class TrenerPlayerAdmin(admin.ModelAdmin):
    pass