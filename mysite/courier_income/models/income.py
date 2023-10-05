from django.db import models


class AbstractIncome(models.Model):

    courier = models.ForeignKey(
        "courier_income.Courier",
        on_delete=models.CASCADE,
        verbose_name="Courier"
    )
    amount = models.PositiveIntegerField(verbose_name="Value", default=0)
    date = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.courier.name} - {self.amount} - {self.date}"


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

    courier = models.ForeignKey(
        "courier_income.Courier",
        on_delete=models.CASCADE,
        related_name="forfeits",
        verbose_name="Courier"
    )


class DailyIncome(AbstractIncome):

    courier = models.ForeignKey(
        "courier_income.Courier",
        on_delete=models.CASCADE,
        related_name="daily_incomes",
        verbose_name="Courier"
    )
    date = models.DateField(unique=True)
