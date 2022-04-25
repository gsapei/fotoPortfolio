from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from PIL import Image

# Create your models here.

class Foto(models.Model):
    titulo = CharField(max_length=120)
    descripcion = CharField(max_length=250)
    imagen = ImageField(upload_to='portfolio/fotos')

    def save(self):
            if not self.imagen:
                return

            super(Foto, self).save()
            fixed_alto = 900 # altura esperada
            image = Image.open(self.imagen)
            ancho, alto = image.size
            if alto > fixed_alto:
                ratio_height = (fixed_alto / alto)
                ancho_calculado = int((float(ancho) * float(ratio_height)))
                size = ( ancho_calculado, fixed_alto )
                image = image.resize(size, Image.ANTIALIAS)
                image.save(self.imagen.path)