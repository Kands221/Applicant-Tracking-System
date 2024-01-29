# ats/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views # adjust import based on where your home view is located
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('job_posting.urls')),  # Includes all URLs from job_posting
    path('apply/', include('applicant_management.urls')),
    path('account/', include('account.urls')),
    path('', views.home, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)