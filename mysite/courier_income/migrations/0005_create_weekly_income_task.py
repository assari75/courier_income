from django.db import migrations

from django_celery_beat import models


def create_weekly_income_task(apps, schema_editor):

    schedule, _ = models.CrontabSchedule.objects.get_or_create(
        minute='0',
        hour='6',
        day_of_week='6',
        day_of_month='*',
        month_of_year='*',
    )
    models.PeriodicTask.objects.create(
        crontab=schedule,
        name="Create Weekly Income Records For Last Week",
        task="create_weekly_income_records_for_last_week"
    )


class Migration(migrations.Migration):

    dependencies = [
        ('courier_income', '0004_weeklyincome'),
        ('django_celery_beat', '0018_improve_crontab_helptext'),
    ]

    operations = [
        migrations.RunPython(create_weekly_income_task),
    ]
