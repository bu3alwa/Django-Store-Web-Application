from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models.manager import EmptyManager
from authentication.models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .choices import *
from store.models import SubscriptionModel
       

class Profile(models.Model):
    #model
    address = models.CharField(_("Address"), max_length=50)
    city = models.CharField(_("City"),max_length=50)

    country = models.CharField(_("Country"), 
            max_length=2, 
            choices=COUNTRY_CHOICES)

    regex=r'\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$'
    phone_validator = RegexValidator(regex=regex, message="Phone number must be in the form of '+9651234567'.") 

    phone_number = models.CharField(_("Phone Number"),
            max_length=17,
            validators=[phone_validator])

    date_of_birth = models.DateField(_("Date of Birth"))

    created_at = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    user = models.OneToOneField(
            settings.AUTH_USER_MODEL, 
            on_delete=models.CASCADE)

    @property
    def full_address(self):
        "Returns users full address."
        return "%s %s %s" % (self.address, self.city, self.country)

class Subscription(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, 
            on_delete=models.CASCADE)

    subscription = models.OneToOneField(
            SubscriptionModel,
            on_delete=models.CASCADE)

    renew = models.BooleanField()


    created_at = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()


