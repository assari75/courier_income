# Generated by Django 4.2.6 on 2023-10-05 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Courier',
                'verbose_name_plural': 'Couriers',
            },
        ),
        migrations.CreateModel(
            name='TripIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Amount')),
                ('date', models.DateField()),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_incomes', to='courier_income.courier', verbose_name='Courier')),
            ],
            options={
                'verbose_name': 'Trip Income',
                'verbose_name_plural': 'Trip Incomes',
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Amount')),
                ('date', models.DateField()),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='courier_income.courier', verbose_name='Courier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Forfeit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Amount')),
                ('date', models.DateField()),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forfeits', to='courier_income.courier', verbose_name='Courier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DailyIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Amount')),
                ('date', models.DateField()),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_incomes', to='courier_income.courier', verbose_name='Courier')),
            ],
        ),
    ]
