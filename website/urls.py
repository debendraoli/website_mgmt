from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('careers/', views.careers, name='careers'),
    path('careers/job/<int:job_id>/', views.job_detail, name='job-detail'),
    path('about-us/', views.job_detail, name='about-us'),
    path('contact/', views.contact, name='contact')
]
