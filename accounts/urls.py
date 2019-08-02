from django.urls import path, include
from accounts import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('create_team', views.create_team, name='create_team'),
    path('manage_teams', views.manage_teams, name='manage_teams'),
    path('teams/<int:team_id>', views.team, name='team'),
    path('teams/<int:team_id>/delete_team', views.delete_team, name='delete_team'),
    path('teams/<int:team_id>/update_team', views.update_team, name='update_team'),
]