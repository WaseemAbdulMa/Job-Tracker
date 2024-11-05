from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name='applications/login.html'), name='login'),
#  path('login/', auth_views.LoginView.as_view(template_name='applications/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('application/add/', views.job_application_add, name='job_application_add'),
    path('application/', views.job_application_list, name='job_application_list'),
    path('todays_applications/', views.todays_applications_view, name='todays_applications'),
    path('application/<int:pk>/', views.job_application_detail, name='job_application_detail'),
    path('application/edit/<int:pk>/', views.job_application_edit, name='job_application_edit'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upcoming-interviews/', views.upcoming_interviews_view, name='upcoming_interviews'),
    path('rejected_companies/', views.rejected_companies_view, name='rejected_companies'),
    path('shortlisted_companies/', views.shortlisted_applications_view, name='shortlisted_companies'),
    path('add-question/', views.add_question, name='add_questions'),
    path('interview-questions/', views.interview_questions, name='interview_questions'),  # New URL for displaying questions
    path('logout/', views.logout_view, name='logout'),





]
