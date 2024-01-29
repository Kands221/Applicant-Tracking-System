# applicant_management/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('job/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
]
