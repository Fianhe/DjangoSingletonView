from django.db import models
import os
from django.conf import settings

class SingletonModel(models.Model):
    name = models.CharField(max_length=10)