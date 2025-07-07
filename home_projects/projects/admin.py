from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'due_date', 'display_assigned_to', 'created_at')
    list_filter = ('area', 'assigned_to', 'due_date')
    search_fields = ('name', 'description', 'area')
    date_hierarchy = 'due_date'
    filter_horizontal = ('assigned_to',) # Use a nice interface for ManyToMany field

    def display_assigned_to(self, obj):
        """Creates a comma-separated string of assigned users for list_display."""
        return ", ".join([user.username for user in obj.assigned_to.all()])
    display_assigned_to.short_description = 'Assigned To' # Column header in admin list
