from django.contrib import admin

from . import models


admin.site.register(models.Courier)
admin.site.register(models.TripIncome)
admin.site.register(models.Reward)
admin.site.register(models.Forfeit)
