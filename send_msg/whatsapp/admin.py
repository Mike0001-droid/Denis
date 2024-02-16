from django.contrib import admin
from .models import BookOfPhone

@admin.register(BookOfPhone)
class BookOfPhoneAdmin(admin.ModelAdmin):
    pass