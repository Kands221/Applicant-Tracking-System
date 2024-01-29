from django import forms
from .models import Job

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'type']  # Adjust the fields based on your Job model
        # You can add widgets here if you want to customize the form fields

class CVUploadForm(forms.Form):
    cv_file = forms.FileField(label='Upload Your CV', widget=forms.ClearableFileInput(attrs={'accept': '.pdf'}))