# Generated by Django 4.2.6 on 2023-10-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier_income', '0002_alter_dailyincome_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyincome',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Amount'),
        ),
    ]