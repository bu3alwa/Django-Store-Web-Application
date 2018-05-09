from django import forms
from .choices import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import UserCreationForm
from datetime import date
from .models import Profile
from store.models import SubscriptionModel
from payment.choices import *

class ProfileForm(forms.ModelForm):
    address = forms.CharField(
            label=_('Address'), 
            max_length=50,
            required=True,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Address'
                    })
            )

    city = forms.CharField(
            label=_('City'), 
            max_length=50,
            required=True,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'City'
                    })
            )

    country = forms.ChoiceField(
            label=_('Country'), 
            required=True,
            choices=COUNTRY_CHOICES,
            widget=forms.Select(
                attrs={
                    'class': 'custom-select',
                    'placeholder': 'Country',
                    }),
            )

    phone_number = forms.CharField(
            label=_('Phone Number'),
            required=True,
            max_length=17,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone Number',
                    })
                )

    date_of_birth = forms.DateField(
            label=_('Date of Birth'),
            widget=forms.SelectDateWidget(
                years=YEARS,
                attrs={
                    'class': 'custom-select',
                    })
            )


    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')

        if date_of_birth is None:
            raise ValidationError(_("No Date of Birth provided"))

        today = date.today()

        if date_of_birth > today:
            raise ValidationError(_("Date of Birth invalid"))

        age_minimum = today.replace(year=(today.year-13))

        if date_of_birth > age_minimum:
            raise ValidationError(_("Must be over 13"))

        return date_of_birth

    def clean(self):
        cleaned_data = super().clean()
        date_of_birth = cleaned_data.get("date_of_brith")
  
    class Meta:
        model = Profile
        exclude = ['user']
        
        
class BillingForm(forms.Form):
    submodel = SubscriptionModel.objects.all()
    submodel = submodel.exclude(length='14')


    subscription_type = forms.ChoiceField(
            label=_("Subscription"),
            choices=((x.id, x.name + ' for ' + x.price + " KD") for x in submodel),
            widget=forms.Select(
                attrs={
                    'class': 'custom-select',
                    }),
                )

    payment_options = forms.ChoiceField(
            label=_("Payment options"),
            choices=PAYMENT_OPTIONS,
            widget=forms.RadioSelect(
                attrs={
                    'class': 'form-check',
                    }),
                )
