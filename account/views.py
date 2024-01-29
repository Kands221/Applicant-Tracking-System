from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import UserRegistrationForm
from .forms import ApplicantProfileForm
from .models import ApplicantProfile
from django.contrib.auth.decorators import login_required
from .models import EmployerProfile, UserProfile

@login_required
def job_seeker_profile(request):
    profile, created = ApplicantProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ApplicantProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('job_seeker_detail', pk=request.user.pk)
    else:
        form = ApplicantProfileForm(instance=profile)
    return render(request, 'account/edit_applicant_profile.html', {'form': form})

def profile_view(request):
    try:
        if request.user.applicantprofile:
            profile = request.user.applicantprofile
            # Render applicant profile template
    except ApplicantProfile.DoesNotExist:
        try:
            if request.user.employerprofile:
                profile = request.user.employerprofile
                # Render employer profile template
        except EmployerProfile.DoesNotExist:
            # Handle case where profile doesn't exist
            pass
    return render(request, 'account/view_profile.html', {'profile': profile})


from django.shortcuts import render, get_object_or_404
from .models import ApplicantProfile, EmployerProfile

def job_seeker_detail(request, pk):
    profile = get_object_or_404(ApplicantProfile, user_id=pk)
    return render(request, 'account/view_job_seeker_profile.html', {'profile': profile})

def employer_profile_detail(request, pk):
    profile = get_object_or_404(EmployerProfile, user_id=pk)
    return render(request, 'account/employer_profile_detail.html', {'profile': profile})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            if role == 'employer':
                EmployerProfile.objects.get_or_create(user=user)
            elif role == 'applicant':
                ApplicantProfile.objects.get_or_create(user=user)
            # Redirect or further processing
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})





def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a home page or another appropriate page
            else:
                # Invalid login error handling
                pass
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page or login page after logout



from django.shortcuts import render, redirect
from .forms import EmployerProfileForm, ApplicantProfileForm
from .models import EmployerProfile, ApplicantProfile
from django.contrib.auth.decorators import login_required

@login_required
def edit_employer_profile(request):
    profile, created = EmployerProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = EmployerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('employer_profile_detail', pk=request.user.pk)
    else:
        form = EmployerProfileForm(instance=profile)

    return render(request, 'account/edit_employer_profile.html', {'form': form})

@login_required
def edit_applicant_profile(request):
    profile, created = ApplicantProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ApplicantProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('applicant_profile_detail', pk=request.user.pk)
    else:
        form = ApplicantProfileForm(instance=profile)

    return render(request, 'account/edit_applicant_profile.html', {'form': form})




