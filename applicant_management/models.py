# applicant_management/models.py

from django.db import models
from job_posting.models import Job

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    resume = models.FileField(upload_to='resumes/')  # Ensure MEDIA_ROOT is set in settings

    def __str__(self):
        return self.name

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Applied')  # Applied, Reviewed, Interview, Offered, Rejected
    applied_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.name} - {self.job.title}"