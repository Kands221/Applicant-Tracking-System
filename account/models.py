# models.py in your app (e.g., users/models.py)

from django.db import models
from django.contrib.auth.models import User

class ApplicantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    skills = models.TextField()
    experience = models.TextField()
    # Add other fields as necessary

    def __str__(self):
        return self.user.username

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    # Add other employer-specific fields here

    def __str__(self):
        return self.company_name  # or return self.company_name if you prefer
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

