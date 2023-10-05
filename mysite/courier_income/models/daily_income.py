from django.db import models


class DailyIncome(models.Model):

    courier = models.ForeignKey(
        "courier_income.Courier",
        on_delete=models.CASCADE,
        related_name="daily_incomes",
        verbose_name="Courier"
    )
    amount = models.PositiveIntegerField(verbose_name="Amount", default=0)
    date = models.DateField()

    class Meta:
        unique_together = ['courier', 'date']

    def __str__(self):
        return f"{self.courier.name} - {self.amount} - {self.date}"
