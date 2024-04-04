from django.shortcuts import render

# Create your views here.
def landpage(request):
    return render(request,'crmland.html')