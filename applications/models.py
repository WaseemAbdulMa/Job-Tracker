from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview Scheduled', 'Interview Scheduled'),
        ('Rejected', 'Rejected'),
        ('Offer', 'Offer'),
        ('Follow-up', 'Follow-up'),
        ('shortlisted', 'Shortlisted'),
    ]
    
    PLATFORM_CHOICES = [
        ('LinkedIn', 'LinkedIn'),
        ('Indeed', 'Indeed'),
        ('Naukri', 'Naukri'),
        ('Glassdoor', 'Glassdoor'),
        ('Email', 'Email'),
        ('Hirist', 'Hirist'),
        ('Monster', 'Monster'),
        ('SimplyHired', 'SimplyHired'),
        ('CareerBuilder', 'CareerBuilder'),
        ('Other', 'Other'),
    ]
    
    RESPONSE_CHOICES = [
        ('pending', 'Pending'),
        ('shortlisted', 'Shortlisted'),
        ('not_selected', 'Not Selected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    date_applied = models.DateField()
    job_description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Applied')
    follow_up_date = models.DateField(null=True, blank=True)
    response_details = models.TextField(blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)
    applied_platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, default='Other')
    interview_date = models.DateField(null=True, blank=True)  # New field for interview date


    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
    class Meta:
        ordering = ['-date_applied']

class InterviewQuestion(models.Model):
    company_name = models.CharField(max_length=255)
    question_text = models.TextField()
    created_at = models.DateTimeField(null=True)  # Automatically set to now when created
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)  # Optional: link to user

    def __str__(self):
        return f"{self.company_name}: {self.question_text}"