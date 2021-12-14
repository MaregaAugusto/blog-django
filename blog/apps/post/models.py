from django.db import models
from django.contrib.auth.models import User
from apps.utils.enum.categorias import Categorias

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    titulo = models.CharField(max_length=250)
    fecha = models.DateField(auto_now_add=True)
    texto = models.TextField()
    categoria = models.CharField(max_length=40, choices=Categorias, default='Pobreza')
    image = models.ImageField(upload_to='post', null=True)

class Comentario(models.Model):
    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateField(auto_now_add=True)
