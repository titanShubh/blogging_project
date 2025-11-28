from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("event_type", "post", "user", "created_at")
    list_filter = ("event_type",)
