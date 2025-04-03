# from django.db import models

# # Create your models here.
# class Job(models.Model):
#     JobTitle = models.CharField(max_length=200)
#     CompanyName = models.CharField(max_length=250)
#     Location = models.CharField(max_length=100)
#     JobType = models.CharField(max_length=100)
#     ApplicationDeadline = models.DateField()
#     JobDescription = models.TextField(max_length=2500)

# models.py
from django.db import models

class JobPosting(models.Model):
    JOB_TYPE_CHOICES = [
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ]
    
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    salary_range = models.CharField(max_length=100)
    job_description = models.TextField()
    # requirements = models.TextField()
    # responsibilities = models.TextField()
    application_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
