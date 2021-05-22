from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('club/getresources/', views.getresources, name='resources'),
    path('club/getmeeting/', views.getmeeting, name='meeting'),
    path('club/meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
]