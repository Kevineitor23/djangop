from django.db import models


class Reclutador(models.Model):
    name = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=250)
    contacto = models.CharField(max_length=100)
    
    