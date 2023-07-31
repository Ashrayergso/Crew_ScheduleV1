```python
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance
from .forms import AssignmentForm

def crewmember_list(request):
    crewmembers = CrewMember.objects.all()
    return render(request, 'crew_assignment_app/crewmember_list.html', {'crewmembers': crewmembers})

def crewmember_detail(request, pk):
    crewmember = get_object_or_404(CrewMember, pk=pk)
    return render(request, 'crew_assignment_app/crewmember_detail.html', {'crewmember': crewmember})

def ship_list(request):
    ships = Ship.objects.all()
    return render(request, 'crew_assignment_app/ship_list.html', {'ships': ships})

def ship_detail(request, pk):
    ship = get_object_or_404(Ship, pk=pk)
    return render(request, 'crew_assignment_app/ship_detail.html', {'ship': ship})

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'crew_assignment_app/assignment_list.html', {'assignments': assignments})

def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    return render(request, 'crew_assignment_app/assignment_detail.html', {'assignment': assignment})

def assignment_create(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.save()
            messages.success(request, "ASSIGNMENT_SUCCESS")
            return redirect('assignment_detail', pk=assignment.pk)
    else:
        form = AssignmentForm()
    return render(request, 'crew_assignment_app/assignment_edit.html', {'form': form})

def assignment_edit(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == "POST":
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.save()
            messages.success(request, "ASSIGNMENT_SUCCESS")
            return redirect('assignment_detail', pk=assignment.pk)
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'crew_assignment_app/assignment_edit.html', {'form': form})

def assignCrewToShips(request):
    # Logic for automatic assignment of crew to ships
    # This is a placeholder and needs to be replaced with actual logic
    pass
```