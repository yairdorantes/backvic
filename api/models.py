from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Paciente(AbstractUser):
    username = models.CharField(max_length=200, unique=False)
    ap_paterno = models.CharField(max_length=100,verbose_name="Apellido paterno",default="",blank=True)
    ap_materno = models.CharField(max_length=100,verbose_name="Apellido materno",default="",blank=True)
    celular = models.CharField(max_length=15,verbose_name="Celular",default="",blank=True,unique=True)
    