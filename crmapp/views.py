from django.shortcuts import render

# Create your views here.
def landpage(request):
    return render(request,'crmland.html')

def dashboard(request):
    return render(request,'dashboard.html')

def dashboardc(request):
    dashboard = request.GET.get('dashboard',' ').split(',')
    return render(request,'dashboard.html',{'dashboard':dashboard})

def archivec(request):
    item_ids = request.GET.get('item_ids',' ').split(',')
    return render(request,'archive.html', {'item_ids': item_ids})