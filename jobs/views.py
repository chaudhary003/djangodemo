from django.shortcuts import render
from .models import Job
# Create your views here.
def jobs_list(request):
    jobs=Job.objects.all()
    
