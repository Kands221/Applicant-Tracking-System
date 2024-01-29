# job_posting/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('post-job/', views.post_job, name='post_job'),
]
