from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.landpage,name='landpage'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboardc',views.dashboardc,name='dashboardc'),
    path('archivec',views.archivec,name='archivec'),
]