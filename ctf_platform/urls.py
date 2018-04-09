from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scoreboard', views.scoreboard, name='scoreboard'),
    path('challenge/<int:challenge_id>', views.challenge, name='challenge'),
    path('team/<int:team_id>', views.team, name='team')
]
