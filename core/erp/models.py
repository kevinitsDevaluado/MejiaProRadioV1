from datetime import datetime
from django.conf import settings
from django.db import models
from django.forms import model_to_dict
from audiofield.fields import AudioField
from config.settings import MEDIA_URL, STATIC_URL
from core.erp.choices import gender_choices,gender_unid
from core.erp.validators import vcedula,validacionCantidad,validacionNacimiento,validacionFechaActual,validarLetras,validarLetrass
from core.models import BaseModel

from core.user.models import User

#TABLA MUSIC
class Music(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo', unique=True,validators=[validarLetras])
    price = models.IntegerField(default=1,validators=[validacionCantidad],null=True, blank=False)
    image = models.ImageField(upload_to='image/%Y/%m/%d', null=False, blank=True, verbose_name='Imagen')
    audio_file = models.FileField(
        upload_to='music/%Y/%m/%d', null=True, blank=True, verbose_name='Música')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuario')
    


    def __str__(self):
        return self.title

    def toJSON(self):
        item = model_to_dict(self)
        item['audio_file'] = self.audio_file.url
        item['image'] = self.get_image()        
        item['usuario'] = self.usuario.toJSON()
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Musica'
        verbose_name_plural = 'Musica'
        ordering = ['id']

#TABLA LIVE
class Live(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo', unique=True,validators=[validarLetras])
    link = models.CharField(max_length=500, null=True, blank=True, verbose_name='Link')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuario')
    

    def __str__(self):
        return self.title

    def toJSON(self):
        item = model_to_dict(self)
        return item


    class Meta:
        verbose_name = 'Live'
        verbose_name_plural = 'Lives'
        ordering = ['id']


#PUBLICIDAD

class Advertising(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombres', unique=True,validators=[validarLetras])
    descripcion = models.CharField(max_length=2000, verbose_name='Descripcion', unique=True)
    link = models.CharField(max_length=500, null=True, blank=True, verbose_name='Link')
    image = models.ImageField(upload_to='advertising/%Y/%m/%d', null=False, blank=True, verbose_name='Imagen')
    

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['image'] = self.get_image()

        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')


    class Meta:
        verbose_name = 'Live'
        verbose_name_plural = 'Lives'
        ordering = ['id']

#GALERIA
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    
    def toJSON(self):
        item = model_to_dict(self)
        return item



class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='galery/%Y/%m/%d',null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
    
    
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
