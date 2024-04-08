from django.shortcuts import render

# Create your views here.
def landpage(request):
    return render(request,'crmland.html')

def dashboard(request):
    return render(request,'dashboard.html')

def archive(request):
    return render(request,'archive.html')