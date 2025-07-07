from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView # For a simple redirect to projects list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('home_projects.projects.urls')), # Fixed import path for 'projects' app
    path('', RedirectView.as_view(url='projects/', permanent=True)), # Redirect root to projects list
]
