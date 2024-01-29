from django.contrib import admin
from .models import ApplicantProfile, EmployerProfile

@admin.register(ApplicantProfile)
class ApplicantProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'skills', 'experience')


@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'company_description')

