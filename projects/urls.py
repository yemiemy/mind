from django.contrib import admin
from django.urls import path, include
from projects import views

urlpatterns = [
    path('create', views.create, name='create_project' ),
    path('', views.projects, name='projects' ),
    path('assign_project', views.assign_project, name='assign_project' ),
]