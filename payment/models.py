from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import JSONField
from store.models import SubscriptionModel
import random, string

class GotapTransactions(models.Model):
    charge_id = models.CharField(max_length=255)
    ammount = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    statement_descriptor = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    response = JSONField()
    urlresponse = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True)

    

class KnetTransactions(models.Model):
    ammount = models.CharField(max_length=10)
    currencycode = models.CharField(max_length=3)
    paymentid = models.CharField(max_length=16)
    paid = models.BooleanField(default=False)

    #reponse
    result = models.CharField(max_length=30, blank=True)
    auth = models.CharField(max_length=255, blank=True)
    ref = models.CharField(max_length=255, blank=True)
    postdate = models.DateField(blank=True, null=True)
    transid = models.CharField(max_length=14, blank=True)

    created_at = models.DateField(auto_now_add=True, blank=True)

    reponse = models.TextField(blank=True)
   

class Transactions(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, 
            on_delete=models.PROTECT,
            related_name='Transactions')

    trackid = models.CharField(
            max_length=16, 
            db_index=True, 
            unique=True)

    GotapTransactions = models.OneToOneField(
            GotapTransactions,
            on_delete=models.CASCADE,
            null=True,
            related_name='GotapTransactions')

    KnetTransactions = models.OneToOneField(
            KnetTransactions,
            on_delete=models.CASCADE,
            null=True,
            related_name='KnetTransactions')

    subscription = models.ForeignKey(
            SubscriptionModel,
            on_delete=models.CASCADE,
            related_name='SubscriptionTransactions')

    subscription_updated = models.BooleanField(default=False)


    def _get_unique_trackid(self):
        trackid = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        unique_trackid = trackid
        while Transactions.objects.filter(trackid=unique_trackid).exists():
            unique_trackid = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        return unique_trackid

    def get_absolute_url(self):
        return reverse('KnetTransactions.confirm_payment', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.trackid:
            self.trackid = self._get_unique_trackid()
        super(Transactions, self).save(*args, **kwargs)





