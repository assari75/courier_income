from rest_framework import serializers

from courier_income import models


class CourierSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Courier
        fields = (
            "name",
        )
