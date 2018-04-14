from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        user_lower_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{user_lower_field: username})

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lowercasing the domain part of it and the name.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = email_name.lower() + '@' + domain_part.lower()
        return email



class CustomUser(AbstractUser):
    objects = CustomUserManager()


