from typing import ChainMap
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField

class User(AbstractUser):

    class TypeUserchoice(models.TextChoices):
        ADMIN = 'admin',
        SPECIALIST = 'specialist',
        PERSONAL_CABINET = 'personal_cabinet'

    surname = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    type_user = models.CharField(max_length=50, choices=TypeUserchoice.choices,
                                                default=TypeUserchoice.PERSONAL_CABINET)

