from django.urls import path, include
from accounts import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('create_team', views.create_team, name='create_team'),
]