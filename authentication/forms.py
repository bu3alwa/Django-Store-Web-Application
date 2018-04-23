from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from .models import CustomUser 
from django.forms.fields import Field

setattr(Field, 'is_checkbox', lambda self: isinstance(self.widget, forms.CheckboxInput))

class ForgotPasswordForm(forms.Form):
    Username = forms.CharField(label='Username', max_length=50)

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
            label=_('First Name'), 
            max_length=50,
            required=True,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'First Name'
                    })
            )

    last_name = forms.CharField(
            label=_('Last Name'), 
            max_length=50,
            required=True,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Last Name'
                    })
            )

    email = forms.EmailField(
            label=_('Email'), 
            max_length=50,
            required=True,
            validators=[
                validate_email,
                ],
            widget=forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email'
                    })
            )

    accept_tos = forms.BooleanField(
            label=_("TOS"),
            required=True,
            widget=forms.CheckboxInput(
                attrs={
                    'class': 'checkbox',
                    })
                )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email is None:
            raise ValidationError(_("No email provided"))

        u = CustomUser.objects.filter(email=email)
        if u.count():
            raise ValidationError(_("Email already exists"))

        return email

    def clean_first_name(self):
        if self.cleaned_data.get('first_name') is None:
            raise ValidationError(_("No first name provided"))

        return self.cleaned_data.get('first_name')

    def clean_last_name(self):
        if self.cleaned_data.get('last_name') is None:
            raise ValidationError(_("No last name provided"))

        return self.cleaned_data.get('last_name')

    def clean(self):
        cleaned_data = super().clean()
        first_name = self.clean_first_name()
        last_name = self.clean_last_name()
        email = self.clean_email()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
                    'first_name', 
                    'last_name', 
                    'email')
        
        
