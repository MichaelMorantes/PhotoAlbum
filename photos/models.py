from unicodedata import category
from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nombre


class Foto(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(null=False, blank=False)
    descripcion = models.TextField()

    def __str__(self):
        return f'Descripcion: {self.descripcion} Categoria: {self.categoria} Imagen:{self.imagen}'

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
