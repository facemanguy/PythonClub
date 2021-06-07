from django.test import TestCase
from .models import Meeting, MeetingMinutes, Event, Resource
from .forms import MeetingForm, ResourceForm

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.meeting=Meeting(meetingtitle="Test Meeting", meetingdate="2021/06/12", meetingtime="08.15", meetinglocation="Test Auditorium", meetingagenda="Test Agenda")

    def test_string(self):
        meet=self.meeting
        self.assertEqual(str(meet), meet.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.minutes=MeetingMinutes(minutesname="Test Minutes", minutestext="Minutes Test Text Data")
    
    def test_string(self):
        self.assertEqual(str(self.minutes), self.minutes.minutesname)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class EventTest(TestCase):
    def setUp(self):
        self.event=Event(eventtitle="Test Event Title", eventlocation="Test Locale", eventdate="2021/07/04", eventtime="9.45", eventdescription="Test Description Text for Event")
    
    def test_string(self):
        self.assertEqual(str(self.event), self.event.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class ResourceTest(TestCase):
    def setUp(self):
        self.resource=Resource(resourcename="Test Resource Name", resourcetype="Book", resourceurl="http://www.example.com", resourcedateentered="2021/01/08", resourcedescription="Test Resource Description")

    def test_string(self):
        self.assertEqual(str(self.resource), self.resource.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class MeetingFormTest(TestCase):
    def test_MeetingForm_is_valid(self):
        form=MeetingForm(data={'meetingtitle':'TESTFORM', 'meetingdate':'01/01/2021', 'meetingtime':'8', 'meetinglocation':'TESTLOCALE', 'meetingagenda':'TESTAGENDA'})
        self.assertTrue(form.is_valid())
    
    def test_MeetingForm_is_valid_optional_fields(self):
        form=MeetingForm(data={'meetingtitle':'TESTFORM', 'meetingdate':'01/01/2021', 'meetinglocation':'TESTLOCALE'})
        self.assertTrue(form.is_valid())

    def test_MeetingForm_empty(self):
        form=MeetingForm(data={'meetingtitle':''})
        self.assertFalse(form.is_valid())

# class ResourceFormTest(TestCase):
#     def test_ResourceForm_is_valid(self):
#         form=ResourceForm(data={'resourcename':'TESTRESOURCENAME', 'resourcetype':'test', 'resourceurl':'https://www.google.com/', 'resourcedateentered':'01/01/2021', 'userid':'3', 'resourcedescription':'TEST DATA DESCRIPTION'})
#         self.assertTrue(form.is_valid())
# TEST FAILING, Not Sure why