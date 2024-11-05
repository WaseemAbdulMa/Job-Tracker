from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import JobApplication,InterviewQuestion
from .forms import JobApplicationForm,UserRegistrationForm
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import date



# Create your views here.
def welcome(request):
    return HttpResponse("hello world")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'applications/register.html', {'form': form})

@login_required
def job_application_add(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('job_application_list')
    else:
        form = JobApplicationForm()
    return render(request, 'applications/job_application_form.html', {'form': form})

@login_required
def job_application_list(request):
    applications = JobApplication.objects.filter(user=request.user)
    paginator = Paginator(applications, 5)  # 3 items per page
    
    page_number = request.GET.get('page', 1)  # Default to 1 if page is not provided
    page_obj = paginator.get_page(page_number)  # Handles invalid page numbers automatically
    
    context = {
        'page_obj': page_obj,  # Use page_obj for the template
    }
    
    return render(request, 'applications/job_application_list.html', context)
@login_required
def todays_applications_view(request):
    today = timezone.now().date()
    todays_applications = JobApplication.objects.filter(date_applied=today)
    
    # Set up pagination
    paginator = Paginator(todays_applications, 5)  # 10 applications per page
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'applications/todays_applications.html', {
        'page_obj': page_obj,
    })

@login_required
def job_application_detail(request, pk):
    application = get_object_or_404(JobApplication, pk=pk,user=request.user)
    return render(request, 'applications/job_application_detail.html', {'application': application})

@login_required
def job_application_edit(request, pk):
    application = get_object_or_404(JobApplication, pk=pk,user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('job_application_list')
    else:
        form = JobApplicationForm(instance=application)
    return render(request, 'applications/job_application_form.html', {'form': form})

@login_required
def dashboard(request):
    # Get current user
    user = request.user
    today = timezone.now().date()
    # Count statistics
    total_applications_today = JobApplication.objects.filter(date_applied=today, user=request.user).count()
    total_applications = JobApplication.objects.filter(user=user).count()    
    total_rejected = JobApplication.objects.filter(user=user, status='Rejected').count()
    shortlisted_count = JobApplication.objects.filter(user=request.user, status='shortlisted').count()    
    upcoming_interviews = JobApplication.objects.filter(
        user=request.user,
        status='Interview Scheduled',
        interview_date__gte=date.today()
    )
     # Handle adding interview questions
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        questions = request.POST.getlist('question_text')  # Get all question texts

        for question_text in questions:
            if question_text:  # Ensure the question text is not empty
                InterviewQuestion.objects.create(company_name=company_name, question_text=question_text)

        return redirect('dashboard')  # Redirect to the same dashboard after saving
    
    
    interview_questions = InterviewQuestion.objects.all()  # or any filter that does not use `user`

    
    
    total_upcoming_interviews = upcoming_interviews.count()

    # Prepare a list of companies and interview dates
    interview_details = [(app.company_name, app.interview_date) for app in upcoming_interviews]
    # Pass data to template
    context = {
        'total_applications_today': total_applications_today,
        'total_upcoming_interviews': total_upcoming_interviews,
        'total_applications': total_applications,
        'total_rejected': total_rejected,
        'shortlisted_count': shortlisted_count,
        'interview_details': interview_details,
        'interview_questions': interview_questions,  # Add this line
        'user': user,
        

        
    }
    return render(request, 'applications/dashboard.html', context)

@login_required

def upcoming_interviews_view(request):
    # Filter for interviews that are scheduled for today or in the future
    upcoming_interviews = JobApplication.objects.filter(status='Interview Scheduled',user=request.user ,interview_date__gte=date.today())
    
    return render(request, 'applications/upcoming_interviews.html', {
        'upcoming_interviews': upcoming_interviews,
    })

@login_required
def rejected_companies_view(request):
    rejected_companies = JobApplication.objects.filter(status='Rejected',user=request.user)
    return render(request,'applications/rejected_companies.html',{
        'rejected_companies':rejected_companies,
    })

@login_required
def shortlisted_applications_view(request):
    shortlisted_applications = JobApplication.objects.filter(status='Shortlisted',user=request.user)
    return render(request,'applications/shortlisted_companies.html',{
        'shortlisted_companies':shortlisted_applications,
    })

@login_required
def add_question(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        questions = request.POST.getlist('question_text')  # Get all question texts

        for question_text in questions:
            if question_text:  # Ensure the question text is not empty
                InterviewQuestion.objects.create(
                    company_name=company_name,
                    question_text=question_text,
                    user=request.user  # Associate the question with the logged-in user
                )

        return redirect('interview_questions')
    
    return render(request, 'applications/add_questions.html')

@login_required
def interview_questions(request):
    questions = InterviewQuestion.objects.filter(user=request.user).order_by('company_name')  # Fetch questions for the logged-in user
    return render(request, 'applications/interview_questions.html', {'questions': questions})




@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

























def logout_view(request):
    logout(request)
    return redirect(reverse('login'))