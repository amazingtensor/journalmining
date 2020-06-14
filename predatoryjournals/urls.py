from django.urls import path
from . import views

urlpatterns = [
    path('', views.predatoryjournals_list, name='predatoryjournals_list'),
]