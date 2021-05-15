from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('club/getresources/', views.getresources, name='resources')
]