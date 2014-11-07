from django.contrib import admin
from .models import (
    Project,
    TimeEntry,
)



class TimeEntryInline(admin.StackedInline):
    model = TimeEntry
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [TimeEntryInline]


admin.site.register(Project, ProjectAdmin)
