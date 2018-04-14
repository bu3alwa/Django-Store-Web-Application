from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models.manager import EmptyManager

class SubscriptionModel(models.Model):
    price = models.CharField(max_length=10)
    length = models.CharField(max_length=2)

class Subscription(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, 
            on_delete=models.CASCADE)

    subcription = models.OneToOneField(
            SubscriptionModel,
            on_delete=models.CASCADE)

    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()




