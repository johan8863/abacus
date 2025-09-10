"""models in category module"""

# django
from django.db import models


class Category(models.Model):
    """Class to manage expenses categories"""
    name = models.CharField(verbose_name="Nombre", max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return self.name