from django.shortcuts import render
from home.forms import ReclutadorForms
from home.models import Reclutador


def home(request):
    
    context = {}
    return render(request,'home/home.html', context)
    
    
    
    
    
