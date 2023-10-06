import datetime
from typing import Tuple

from django.db import models

from courier_income.models import Courier, DailyIncome


class WeeklyIncome(models.Model):
    
    # Saturday is the start of the week and is the 5th day of the week in georgian calendar
    START_WEEKDAY = 5 

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

    @classmethod
    def get_last_week_start_and_end_date(cls) -> Tuple[datetime.date, datetime.date]:
        today = datetime.date.today()
        days_until_last_week_start_date = (today.weekday() - cls.START_WEEKDAY) % 7 + 7
        start_date = today - datetime.timedelta(days=days_until_last_week_start_date)
        end_date = start_date + datetime.timedelta(days=6)
        return start_date, end_date

    @classmethod
    def create_last_week_records(cls):
        start_date, end_date = cls.get_last_week_start_and_end_date()
        courier_ids = DailyIncome.objects.get_couriers_with_daily_income_in_a_date_range(
            start_date, end_date
        )
        for courier_id in courier_ids:
            courier = Courier.objects.get(pk=courier_id)
            weekly_income_amount = DailyIncome.objects.get_courier_total_income_in_a_date_range(
                courier, start_date, end_date
            )
            weekly_income, created = cls.objects.get_or_create(courier=courier, start_date=start_date)
            weekly_income.amount = weekly_income_amount
            weekly_income.save()
