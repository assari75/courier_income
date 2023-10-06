import celery

from . import models


@celery.shared_task(name="create_weekly_income_records_for_last_week")
def create_weekly_income_records_for_last_week():
    models.WeeklyIncome.create_last_week_records()
