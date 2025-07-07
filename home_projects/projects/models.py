from django.db import models
from django.contrib.auth.models import User # Django's built-in User model

class Project(models.Model):
    name = models.CharField(max_length=200)
    area = models.CharField(max_length=100, help_text="e.g., Kitchen, Bathroom, Garden")
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    assigned_to = models.ManyToManyField(User, related_name='assigned_projects', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['due_date', 'name'] # Order projects by due date, then name
