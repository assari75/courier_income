from django.db import models


class AbstractIncome(models.Model):

    IS_POSITIVE = True
    
    courier = models.ForeignKey(
        "courier_income.Courier",
        on_delete=models.CASCADE,
        verbose_name="Courier"
    )
    amount = models.PositiveIntegerField(verbose_name="Amount")
    date = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.courier.name} - {self.amount} - {self.date}"

    def create_or_update_daily_income(self):
        daily_income, created = DailyIncome.objects.get_or_create(
            date=self.date,
            courier=self.courier
        )
        if self.IS_POSITIVE:
            daily_income.amount += self.amount
        else:
            daily_income.amount -= self.amount
        daily_income.save()


class TripIncome(AbstractIncome):

    courier = models.ForeignKey(
        "courier_income.Courier",
        on_delete=models.CASCADE,
        related_name="trip_incomes",
        verbose_name="Courier"
    )

    class Meta:
        verbose_name = "Trip Income"
        verbose_name_plural = "Trip Incomes"


class Reward(AbstractIncome):

    courier = models.ForeignKey(
        "courier_income.Courier",
        on_delete=models.CASCADE,
        related_name="rewards",
        verbose_name="Courier"
    )


class Forfeit(AbstractIncome):

    IS_POSITIVE = False

    courier = models.ForeignKey(
        "courier_income.Courier",
        on_delete=models.CASCADE,
        related_name="forfeits",
        verbose_name="Courier"
    )


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
