from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'exercise/(?P<exercise_id>[0-9]+)$', views.exercise, name='exercise')
]
