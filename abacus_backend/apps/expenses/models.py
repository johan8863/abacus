"""models in expenses module"""

# django
from django.db import models

# local
from ..categories.models import Category


class Expense(models.Model):
    """class to manage expenses in the software"""
    name = models.CharField(verbose_name="Nombre", max_length=120)
    cost = models.DecimalField(verbose_name="Importe", max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_created_auto = models.BooleanField(default=True)
    is_updated_auto = models.BooleanField(default=True)
    created_manual = models.DateField(null=True, blank=True)
    updated_manual = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"
    
    def __str__(self):
        return self.name
