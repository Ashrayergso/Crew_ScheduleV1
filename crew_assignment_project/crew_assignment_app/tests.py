```python
from django.test import TestCase
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance

class CrewMemberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CrewMember.objects.create(name='John', status='Active', position=Positions.objects.create(position_code='P01', name='Captain'), gender='Male')

    def test_name_label(self):
        crewmember = CrewMember.objects.get(id=1)
        field_label = crewmember._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_status_label(self):
        crewmember = CrewMember.objects.get(id=1)
        field_label = crewmember._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'status')

    def test_position_label(self):
        crewmember = CrewMember.objects.get(id=1)
        field_label = crewmember._meta.get_field('position').verbose_name
        self.assertEquals(field_label, 'position')

    def test_gender_label(self):
        crewmember = CrewMember.objects.get(id=1)
        field_label = crewmember._meta.get_field('gender').verbose_name
        self.assertEquals(field_label, 'gender')

class AssignmentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Assignment.objects.create(crewmember=CrewMember.objects.create(name='John', status='Active', position=Positions.objects.create(position_code='P01', name='Captain'), gender='Male'), ship=Ship.objects.create(name='Ship1', ship_code='S01', brand='Brand1'), start_date='2022-01-01', end_date='2022-12-31', position=Positions.objects.get(id=1))

    def test_crewmember_label(self):
        assignment = Assignment.objects.get(id=1)
        field_label = assignment._meta.get_field('crewmember').verbose_name
        self.assertEquals(field_label, 'crewmember')

    def test_ship_label(self):
        assignment = Assignment.objects.get(id=1)
        field_label = assignment._meta.get_field('ship').verbose_name
        self.assertEquals(field_label, 'ship')

    def test_start_date_label(self):
        assignment = Assignment.objects.get(id=1)
        field_label = assignment._meta.get_field('start_date').verbose_name
        self.assertEquals(field_label, 'start date')

    def test_end_date_label(self):
        assignment = Assignment.objects.get(id=1)
        field_label = assignment._meta.get_field('end_date').verbose_name
        self.assertEquals(field_label, 'end date')

    def test_position_label(self):
        assignment = Assignment.objects.get(id=1)
        field_label = assignment._meta.get_field('position').verbose_name
        self.assertEquals(field_label, 'position')
```