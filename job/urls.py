# job/urls.py
from django.urls import path
from .views import (
    JobListView,
    JobDetailView,
    JobCreateView,
    JobUpdateView,
    JobDeleteView,
    EmployerDashboardView,
)
app_name = "job"

urlpatterns = [
    path("", JobListView.as_view(), name="job_list"),
    path("job/<int:pk>/", JobDetailView.as_view(), name="job_detail"),
    path("job/create/", JobCreateView.as_view(), name="job_create"),
    path("job/<int:pk>/edit/", JobUpdateView.as_view(), name="job_edit"),
    path("job/<int:pk>/delete/", JobDeleteView.as_view(), name="job_delete"),
    path("dashboard/", EmployerDashboardView.as_view(), name="dashboard"),
]
