# applicant_management/views.py

from django.shortcuts import render, redirect
from job_posting.models import Job
from .models import Application
from .forms import ApplicationForm  # We will create this form next

def apply_for_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('some_success_page')  # Redirect to a success page
    else:
        form = ApplicationForm()

    return render(request, 'applicant_management/apply_for_job.html', {'form': form, 'job': job})
