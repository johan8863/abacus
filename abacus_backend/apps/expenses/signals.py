"""signals from expenses module"""

# python
from datetime import datetime

# django
from django.db.models.signals import pre_save
from django.dispatch import receiver

# local
from .models import Expense

@receiver(pre_save, sender=Expense)
def set_expenses_dates(sender, instance, **kwargs):
    """
    Signal handler to set manual dates from auto flags
    """
    now = datetime.now()
    
    # if its a new object
    if not instance.pk:
        if instance.is_created_auto:
            # only assign if not initial value
            # but always set updated_manual
            if not instance.created_manual:
                instance.created_manual = now.date()
                instance.updated_manual = now.date()
    
    # to update
    if instance.is_updated_auto:
        instance.updated_manual = now.date()
