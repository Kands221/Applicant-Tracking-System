from .models import Job
from django.shortcuts import render, redirect
from .models import Job
from .forms import JobPostForm


def job_list(request):
    jobs = Job.objects.all().order_by('-id')
    return render(request, 'job_posting/job_list.html', {'jobs': jobs})


from django.shortcuts import render, get_object_or_404
from .models import Job


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    

    return render(request, 'job_posting/job_detail.html', {'job': job,})



def post_job(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Redirect to job listing page after posting
    else:
        form = JobPostForm()
    return render(request, 'job_posting/post_job.html', {'form': form})

