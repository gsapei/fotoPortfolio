from django.shortcuts import render
from .models import Foto

# Create your views here.

def home(request):
    fotos = Foto.objects.all()
    return render(request,'home.html',{'fotos': fotos})