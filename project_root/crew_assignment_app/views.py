```python
from django.shortcuts import render
from django.contrib import messages
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance

def crewmember_list(request):
    crewmembers = CrewMember.objects.all()
    messages.success(request, "CREW_FETCH_SUCCESS")
    return render(request, 'crew_assignment_app/crewmember_list.html', {'crewmembers': crewmembers})

def crewmember_detail(request, id):
    crewmember = CrewMember.objects.get(id=id)
    return render(request, 'crew_assignment_app/crewmember_detail.html', {'crewmember': crewmember})

def ship_list(request):
    ships = Ship.objects.all()
    messages.success(request, "SHIP_FETCH_SUCCESS")
    return render(request, 'crew_assignment_app/ship_list.html', {'ships': ships})

def ship_detail(request, id):
    ship = Ship.objects.get(id=id)
    return render(request, 'crew_assignment_app/ship_detail.html', {'ship': ship})

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'crew_assignment_app/assignment_list.html', {'assignments': assignments})

def assignment_detail(request, id):
    assignment = Assignment.objects.get(id=id)
    return render(request, 'crew_assignment_app/assignment_detail.html', {'assignment': assignment})

def assignCrewToShips(request):
    # Logic for automatic assignment of crew to ships goes here
    # This is a placeholder and needs to be replaced with actual logic
    messages.success(request, "ASSIGNMENT_SUCCESS")
    return render(request, 'crew_assignment_app/assignment_list.html')
```