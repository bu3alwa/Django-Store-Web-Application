from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models.manager import EmptyManager
from authentication.models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .choices import *



class ProfileManager(models.Manager):
    def create_profile(self, address, city, country, phone_number, date_of_birth, user):
        if not address:
            raise ValueError('Must give an address')
        if not city:
            raise ValueError('Must give a city')
        if not country:
            raise ValueError('Must give a country')
        if not phone_number:
            raise ValueError('Must give a phone number')
        if not date_of_birth:
            raise ValueError('Must have a date of birth')

        profile = self.model(address=address, city=city, country=country, phone_number=phone_number, date_of_birth=date_of_birth, user=user)
        profile.full_clean()
        profile.save()
        return profile
        

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

    objects = ProfileManager()

    @property
    def full_address(self):
        "Returns users full address."
        return "%s %s %s" % (self.address, self.city, self.country)

