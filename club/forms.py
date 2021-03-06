from django import forms
from django.forms import fields
from .models import Meeting, MeetingMinutes, Resource, Event

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'