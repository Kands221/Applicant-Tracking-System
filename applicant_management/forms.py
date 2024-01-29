# applicant_management/forms.py

from django import forms
from .models import Applicant

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'email', 'resume']  # Adjust fields as per your Applicant model
