from email.policy import default
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.forms import IntegerField

# Create your models here.

class Foto(models.Model):
    titulo = CharField(max_length=120)
    descripcion = CharField(max_length=250)
    imagen = ImageField(upload_to='portfolio/fotos')