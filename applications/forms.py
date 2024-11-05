from django import forms
from .models import JobApplication,InterviewQuestion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company_name', 'job_title', 'date_applied', 'job_description', 'status', 'follow_up_date', 'response_details', 'additional_notes','applied_platform','interview_date']
        widgets = {
            'date_applied': forms.DateInput(attrs={'type': 'date'}),
            'interview_date': forms.DateInput(attrs={'type': 'date'}),
            'follow_up_date':forms.DateInput(attrs={'type':'date'}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InterviewQuestionForm(forms.ModelForm):
    class Meta:
        model = InterviewQuestion
        fields = ['company_name', 'question_text']