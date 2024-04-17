from django.shortcuts import render

# Create your views here.
def landpage(request):
    return render(request,'crmland.html')

def dashboardc(request):
    return render(request,'dashboard.html')

def archivec(request):
    return render(request,'archive.html')