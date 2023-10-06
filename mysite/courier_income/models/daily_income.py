from django.db import models


class DailyIncomeQuerySet(models.QuerySet):

    def get_courier_total_income_in_a_date_range(self, courier, start_date, end_date) -> int:
        return self.filter(
            courier=courier,
            date__range=(start_date, end_date)
        ).aggregate(total=models.Sum("amount"))["total"]

    def get_couriers_with_daily_income_in_a_date_range(self, start_date, end_date):
        return self.filter(
            date__range=(start_date, end_date)
        ).values_list("courier", flat=True).distinct()


class DailyIncome(models.Model):

    courier = models.ForeignKey(
        "courier_income.Courier",
        on_delete=models.CASCADE,
        related_name="daily_incomes",
        verbose_name="Courier"
    )
    amount = models.IntegerField(verbose_name="Amount", default=0)
    date = models.DateField()

    objects = models.Manager.from_queryset(DailyIncomeQuerySet)()

    class Meta:
        unique_together = ['courier', 'date']

    def __str__(self):
        return f"{self.courier} - {self.amount} - {self.date}"
