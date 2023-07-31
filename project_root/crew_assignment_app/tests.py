```python
from django.test import TestCase
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance

class CrewMemberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CrewMember.objects.create(name='John', status='Active', position=Positions.objects.create(position_code='P01', name='Captain'), availability_date='2022-12-31')

    def test_name_label(self):
        crewmember = CrewMember.objects.get(id=1)
        field_label = crewmember._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_status_label(self):
        crewmember = CrewMember.objects.get(id=1)
        field_label = crewmember._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'status')

class ShipModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Ship.objects.create(name='Titanic', ship_code='S01', brand='White Star Line')

    def test_name_label(self):
        ship = Ship.objects.get(id=1)
        field_label = ship._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_brand_label(self):
        ship = Ship.objects.get(id=1)
        field_label = ship._meta.get_field('brand').verbose_name
        self.assertEquals(field_label, 'brand')

class AssignmentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Assignment.objects.create(crewmember=CrewMember.objects.create(name='John', status='Active', position=Positions.objects.create(position_code='P01', name='Captain'), availability_date='2022-12-31'), ship=Ship.objects.create(name='Titanic', ship_code='S01', brand='White Star Line'), start_date='2022-01-01', end_date='2022-12-31', position=Positions.objects.get(id=1))

    def test_start_date_label(self):
        assignment = Assignment.objects.get(id=1)
        field_label = assignment._meta.get_field('start_date').verbose_name
        self.assertEquals(field_label, 'start date')

    def test_end_date_label(self):
        assignment = Assignment.objects.get(id=1)
        field_label = assignment._meta.get_field('end_date').verbose_name
        self.assertEquals(field_label, 'end date')
```