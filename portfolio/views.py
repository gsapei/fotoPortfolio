from django.shortcuts import render
from .models import Foto
import random

# Create your views here.

def home(request):
    fotos = Foto.objects.all()
    items = fotos.order_by('?')
    
    return render(request,'home.html',{'fotos': items})