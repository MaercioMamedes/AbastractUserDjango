from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    """A classe MysUser irá herdar todos os atributos e métodos de um UserAdmin padrão do Django"""
    phone = models.CharField("telefone", max_length=11, blank=True)
    profile_image = models.ImageField(blank=True)
