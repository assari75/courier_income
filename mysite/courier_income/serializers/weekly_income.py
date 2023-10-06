from rest_framework import serializers

from courier_income import models
from courier_income.serializers import CourierSerializer


class WeeklyIncomeSerializer(serializers.ModelSerializer):

    courier = CourierSerializer()
    
    class Meta:
        model = models.WeeklyIncome
        fields = (
            "courier",
            "amount",
            "start_date",
        )
