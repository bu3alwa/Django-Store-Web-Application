from django.utils.translation import gettext_lazy as _
from datetime import datetime


COUNTRY_CHOICES = ( 
    ("KW", _("Kuwait")),
    )

year = datetime.now().year
YEARS = [ x for x in range(1940,year)]
