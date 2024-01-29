from .models import Job
from django.shortcuts import render, redirect
from .models import Job
from .forms import JobPostForm


def job_list(request):
    jobs = Job.objects.all().order_by('-id')
    return render(request, 'job_posting/job_list.html', {'jobs': jobs})


from django.shortcuts import render, get_object_or_404
from .models import Job
from .forms import CVUploadForm
import PyPDF2
from io import BytesIO
from .utils import parse_cv

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    text = None
    parsed_data = None
    form = CVUploadForm()

    if request.method == 'POST':
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cv_file = request.FILES['cv_file']
            
            # Read the PDF file
            try:
                pdf_reader = PyPDF2.PdfReader(BytesIO(cv_file.read()))
                text = ''.join([pdf_reader.pages[i].extract_text() for i in range(len(pdf_reader.pages))])
                parsed_data = parse_cv(text)
            except Exception as e:
                text = f"Error reading PDF: {e}"
            # Handle parsed_data as needed
            # For example, saving the text to a model or further processing

    return render(request, 'job_posting/job_detail.html', {'job': job, 'form': form, 'parsed_text': text, 'parsed_data': parsed_data})



def post_job(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Redirect to job listing page after posting
    else:
        form = JobPostForm()
    return render(request, 'job_posting/post_job.html', {'form': form})

