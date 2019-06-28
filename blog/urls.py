"""Importing Django function path and all our views from the 
blog application"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]