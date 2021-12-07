from django.db import models
from apps.utils.enum.categorias import Categorias

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=250)
    fecha = models.DateField(auto_now_add=True)
    texto = models.TextField()
    categoria = models.CharField(max_length=40, choices=Categorias, default='Pobreza')
    image = models.ImageField()

class Comentario(models.Model):
    #usuario = models.ForeignKey(Usuario, on_delete=models.)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comentario = models.TextField()
    class Meta:
        ordering = ["-id"]
