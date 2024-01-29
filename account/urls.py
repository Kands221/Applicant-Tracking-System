# urls.py

from django.urls import path
from . import views  # Adjust as per your views

urlpatterns = [
    # ... other url patterns ...
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Adjust view names as necessary
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='job_seeker_profile'),
    path('profile/employer/<int:pk>/', views.employer_profile_detail, name='employer_profile_detail'),
    path('profile/applicant/<int:pk>/', views.job_seeker_detail, name='applicant_profile_detail'),
    path('profile/employer/edit', views.edit_employer_profile, name='edit_employer_profile'),
    path('profile/applicant/edit', views.edit_applicant_profile, name='edit_applicant_profile'),
]


