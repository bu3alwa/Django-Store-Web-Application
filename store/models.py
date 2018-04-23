from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models.manager import EmptyManager

class SubscriptionModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    length = models.CharField(max_length=2)

