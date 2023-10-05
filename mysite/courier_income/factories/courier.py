import factory

from courier_income import models


class CourierFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Courier
    
    name = factory.Faker("name")
