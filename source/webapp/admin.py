from django.contrib import admin
from .models import Mission, Status, Type, Project


class MissionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'summary', 'status', 'created_at']
    list_filter = ['status', 'type']
    list_display_links = ['pk', 'summary']
    search_fields = ['summary', 'description']
    exclude = []
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Mission)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)
