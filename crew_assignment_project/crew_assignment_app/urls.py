```python
from django.urls import path
from . import views

app_name = 'crew_assignment_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('crewmembers/', views.CrewMemberListView.as_view(), name='crewmembers'),
    path('crewmembers/<int:pk>', views.CrewMemberDetailView.as_view(), name='crewmember-detail'),
    path('ships/', views.ShipListView.as_view(), name='ships'),
    path('ships/<int:pk>', views.ShipDetailView.as_view(), name='ship-detail'),
    path('assignments/', views.AssignmentListView.as_view(), name='assignments'),
    path('assignments/<int:pk>', views.AssignmentDetailView.as_view(), name='assignment-detail'),
    path('assignments/create/', views.AssignmentCreateView.as_view(), name='assignment-create'),
    path('assignments/<int:pk>/edit/', views.AssignmentUpdateView.as_view(), name='assignment-edit'),
    path('assign/', views.assignCrewToShips, name='assign-crew'),
]
```