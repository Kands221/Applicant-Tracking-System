from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ApplicantProfile, EmployerProfile

from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    ROLE_CHOICES = (
        ('employer', 'Employer'),
        ('applicant', 'Applicant'),
    )

    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        role = self.cleaned_data['role']
        if commit:
            user.save()
            if role == 'employer':
                EmployerProfile.objects.get_or_create(user=user)
            elif role == 'applicant':
                ApplicantProfile.objects.get_or_create(user=user)
        return user


class ApplicantProfileForm(forms.ModelForm):
    class Meta:
        model = ApplicantProfile
        fields = ['skills', 'experience', 'resume']




class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'company_description']

