```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crewmember/', views.CrewMemberListView.as_view(), name='crewmember'),
    path('crewmember/<int:pk>', views.CrewMemberDetailView.as_view(), name='crewmember-detail'),
    path('ship/', views.ShipListView.as_view(), name='ship'),
    path('ship/<int:pk>', views.ShipDetailView.as_view(), name='ship-detail'),
    path('assignment/', views.AssignmentListView.as_view(), name='assignment'),
    path('assignment/<int:pk>', views.AssignmentDetailView.as_view(), name='assignment-detail'),
    path('assignment/create/', views.AssignmentCreate.as_view(), name='assignment-create'),
    path('assignment/<int:pk>/edit/', views.AssignmentUpdate.as_view(), name='assignment-update'),
    path('assignCrewToShips/', views.assignCrewToShips, name='assign-crew-to-ships'),
]
```