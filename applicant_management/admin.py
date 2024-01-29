# applicant_management/admin.py

from django.contrib import admin
from .models import Applicant, Application

admin.site.register(Applicant)
admin.site.register(Application)
