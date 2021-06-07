from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('club/getresources/', views.getresources, name='resources'),
    path('club/getmeeting/', views.getmeeting, name='meeting'),
    path('club/meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    path('club/newmeeting', views.newMeeting, name='newmeeting'),
    path('club/newresource', views.newResource, name='newresource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]