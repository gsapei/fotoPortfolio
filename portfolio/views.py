from django.shortcuts import get_object_or_404, render
from .models import Foto
import random

# Create your views here.

def about(request):
    return render(request,'about.html')

def home(request):
    fotos = Foto.objects.all()
    items = fotos.order_by('?')
    
    return render(request,'home.html',{'fotos': items})

def detalle_foto(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)
    return render(request, 'detalleFoto.html', {"foto": foto})