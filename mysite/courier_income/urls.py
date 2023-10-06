from django.urls import path

from . import views


app_name = 'courier_income'


urlpatterns = [
     path(
          'weekly',
          views.WeeklyIncomeList.as_view(),
          name="weekly-income-list"
     ),
]
