from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'pages/home.html')
def index(request):
    return render(request,'pages/index.html')
def about(request):
    name='arvind'
    context={'n':name}
    return render(request,'pages/about.html',context)
