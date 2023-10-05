import datetime
from typing import List

from django.db import models


class WeeklyIncome(models.Model):

    courier = models.ForeignKey(
        "courier_income.Courier",
        on_delete=models.CASCADE,
        related_name="weekly_incomes",
        verbose_name="Courier"
    )
    amount = models.IntegerField(verbose_name="Amount", default=0)
    start_date = models.DateField()

    class Meta:
        unique_together = ['courier', 'start_date']

    def __str__(self):
        return f"{self.courier} - {self.amount} - {self.start_date}"
