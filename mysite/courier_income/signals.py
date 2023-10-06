from django.db.models import signals
from django.dispatch import receiver

from . import models


@receiver(signals.post_save, sender=models.TripIncome)
@receiver(signals.post_save, sender=models.Reward)
@receiver(signals.post_save, sender=models.Forfeit)
def create_or_update_daily_income(sender, instance, **kwargs):
    instance.create_or_update_daily_income()
