from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='myhome'),
    path('index.html', views.home, name='myhome'),
    path('about.html', views.about, name='myabout'),
    path('contact.html', views.contact, name='mycontact'),
    path('formdata', views.formdata, name='myform')
]