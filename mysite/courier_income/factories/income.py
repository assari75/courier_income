import datetime

import factory
import factory.fuzzy

from courier_income import models


class AbstractIncomeFactory(factory.django.DjangoModelFactory):

    class Meta:
        abstract = True

    courier = factory.SubFactory("courier_income.factories.CourierFactory")
    amount = factory.fuzzy.FuzzyInteger(low=0, high=2147483647)
    date = factory.fuzzy.FuzzyDate(start_date=datetime.date(2020, 1, 1))


class TripIncomeFactory(AbstractIncomeFactory):

    class Meta:
        model = models.TripIncome


class RewardFactory(AbstractIncomeFactory):

    class Meta:
        model = models.Reward


class ForfeitFactory(AbstractIncomeFactory):

    class Meta:
        model = models.Forfeit


class DailyIncomeFactory(AbstractIncomeFactory):

    class Meta:
        model = models.DailyIncome
