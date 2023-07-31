```python
from django.db import models

class Positions(models.Model):
    position_code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)

class Cert(models.Model):
    name = models.CharField(max_length=200)
    issuing_authority = models.CharField(max_length=200)
    expiry_date = models.DateField()
    validity_days = models.IntegerField()

class Qualification(models.Model):
    name = models.CharField(max_length=200)
    required_certificates = models.ManyToManyField(Cert)

class Ship(models.Model):
    name = models.CharField(max_length=200)
    ship_code = models.CharField(max_length=50)
    brand = models.CharField(max_length=200)

class CrewMember(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    certificates = models.ManyToManyField(Cert)
    qualifications = models.ManyToManyField(Qualification)
    availability_date = models.DateField()
    gender = models.CharField(max_length=10)

class Assignment(models.Model):
    crewmember = models.ForeignKey(CrewMember, on_delete=models.CASCADE)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)

class ShipCrewAllowance(models.Model):
    ship_code = models.ForeignKey(Ship, on_delete=models.CASCADE)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    quantity = models.IntegerField()
```