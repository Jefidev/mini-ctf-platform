from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'challenge/(?P<challenge_id>\d)$', views.challenge, name='challenge'),
]
