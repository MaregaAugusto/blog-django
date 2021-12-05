from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=250)
    description = models.TextField()

class Comentario(models.Model):
    description = models.TextField()
