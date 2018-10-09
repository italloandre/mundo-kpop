
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Contato(models.Model):
    email = models.CharField(max_length=200, null=False)
    texto = models.TextField()
    assunto = models.CharField(max_length=500)