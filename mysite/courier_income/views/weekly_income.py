from rest_framework import generics, exceptions

from courier_income import models, serializers


class WeeklyIncomeList(generics.ListAPIView):
    
    queryset = models.WeeklyIncome.objects.all()
    serializer_class = serializers.WeeklyIncomeSerializer

    def get_queryset(self):
        serializer = serializers.DateRangeSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        from_date = serializer.validated_data["from_date"]
        to_date = serializer.validated_data["to_date"]
        return models.WeeklyIncome.objects.filter(
            start_date__range=(from_date, to_date)
        )
