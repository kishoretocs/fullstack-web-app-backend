# urls.py
from django.urls import path
from .views import job_list

urlpatterns = [
    path('api/jobs/', job_list, name='job_list'),
]
