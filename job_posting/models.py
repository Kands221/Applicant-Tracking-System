# job_posting/models.py

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_on = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  # e.g., Full-time, Part-time

    def __str__(self):
        return self.title