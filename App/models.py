from django.db import models

from .forms import *


class Passinger(models.Model):
    sNo = models.IntegerField()
    name = models.CharField(max_length=70)
    mailId = models.EmailField()
    password = models.CharField(max_length=99)
    photo = models.ImageField()
    dot = models.DateField()
    persons = models.IntegerField()
    cost = models.IntegerField()
