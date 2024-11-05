# Generated by Django 4.2.16 on 2024-11-02 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('date_applied', models.DateField()),
                ('job_description', models.TextField()),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Interview Scheduled', 'Interview Scheduled'), ('Rejected', 'Rejected'), ('Offer', 'Offer'), ('Follow-up', 'Follow-up'), ('shortlisted', 'Shortlisted')], default='Applied', max_length=50)),
                ('follow_up_date', models.DateField(blank=True, null=True)),
                ('response_details', models.TextField(blank=True, null=True)),
                ('additional_notes', models.TextField(blank=True, null=True)),
                ('applied_platform', models.CharField(choices=[('LinkedIn', 'LinkedIn'), ('Indeed', 'Indeed'), ('Naukri', 'Naukri'), ('Glassdoor', 'Glassdoor'), ('Email', 'Email'), ('Hirist', 'Hirist'), ('Monster', 'Monster'), ('SimplyHired', 'SimplyHired'), ('CareerBuilder', 'CareerBuilder'), ('Other', 'Other')], default='Other', max_length=50)),
                ('interview_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('question_text', models.TextField()),
                ('created_at', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
