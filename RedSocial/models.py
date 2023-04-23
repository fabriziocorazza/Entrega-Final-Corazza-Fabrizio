from django.db import models
from django.contrib.auth.models import User

class PostSeries(models.Model):
    Nombre_de_la_serie = models.CharField(max_length=20)
    Platamormas = models.CharField(max_length=20)
    Descripcion_de_la_serie= models.TextField(max_length=500)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    imagen = models.ImageField(upload_to="posts", null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.Nombre_de_la_serie} --- {self.Platamormas}"
    

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    email = models.EmailField(max_length = 254)
    imagen = models.ImageField(upload_to="profiles", null=True, blank=True)

class Mensajes(models.Model):
    asunto = models.CharField(max_length=20)
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    Destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="destinatario")