from django.shortcuts import get_object_or_404, render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def getresources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})

def getmeeting(request):
    meeting_list=Meeting.objects.all()    
    return render(request, 'club/meeting.html', {'meeting_list' : meeting_list})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetail.html', {'meet' : meet})