from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
# Create your views here.

class HomePageView(TemplateView):
    template_name='home.html'


    