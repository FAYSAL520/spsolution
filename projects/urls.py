from django.urls import path
from . import views
from django.contrib import admin


admin.site.site_header = "FS Search Admin"
admin.site.site_title = "FS Search Admin Panel"
admin.site.index_title = "Welcome to FS Search Admin Panel"

urlpatterns = [
    path('', views.projects, name="projects"),
    path('/<str:pk>', views.project, name="project"),

    path('create-project', views.createProject, name="create-project"),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),
    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),
]
