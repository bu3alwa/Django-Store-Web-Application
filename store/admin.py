from django.contrib import admin
from .models import SubscriptionModel

# Register your models here.

class SubscriptionModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(SubscriptionModel, SubscriptionModelAdmin)


