# Generated by Django 4.2.6 on 2023-10-05 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courier_income', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Value')),
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
                ('amount', models.PositiveIntegerField(verbose_name='Value')),
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
                ('amount', models.PositiveIntegerField(verbose_name='Value')),
                ('date', models.DateField()),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forfeits', to='courier_income.courier', verbose_name='Courier')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
