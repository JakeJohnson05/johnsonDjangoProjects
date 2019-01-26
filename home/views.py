from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import JohnsonApp

class HomeView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'appList'
    
    def get_queryset(self):
        """ returns all the apps """
        return JohnsonApp.objects.all()