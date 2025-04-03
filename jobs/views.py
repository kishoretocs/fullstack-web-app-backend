# views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import JobPosting
from .forms import JobPostingForm

@csrf_exempt  # For testing purposes; in production, consider using proper CSRF handling
def job_list(request):
    if request.method == 'GET':
        # Optional filtering based on query parameters
        filters = {}
        job_title = request.GET.get('job_title')
        location = request.GET.get('location')
        job_type = request.GET.get('job_type')
        salary_range = request.GET.get('salary_range')
        
        if job_title:
            filters['job_title__icontains'] = job_title
        if location:
            filters['location__icontains'] = location
        if job_type:
            filters['job_type'] = job_type
        if salary_range:
            filters['salary_range__icontains'] = salary_range
        
        jobs = JobPosting.objects.filter(**filters).values()
        return JsonResponse(list(jobs), safe=False)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        form = JobPostingForm(data)
        print('-----------',data)
        print('===============',request.body)
        if form.is_valid():
            job = form.save()
            return JsonResponse({"id": job.id}, status=201)
        else:
            return JsonResponse(form.errors, status=400)
    
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
