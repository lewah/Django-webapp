from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('patner/',views.patner,name='patner'),
    path('demo/',views.demo,name='demo'),
    path('contactus/',views.contactus,name='contactus'),
    
]