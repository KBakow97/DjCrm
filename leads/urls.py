from django.urls import path
from .views import (
    lead_list, lead_detail, lead_create, lead_update, lead_delete,
    LeadListView, LandingDetailView, LandingCreateView, LandingUpdateView, LandingDeleteView
)

app_name = "leads"
urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LandingDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LandingUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LandingDeleteView.as_view(), name='lead-delete'),
    path('create/', LandingCreateView.as_view(), name='lead-create')
]
