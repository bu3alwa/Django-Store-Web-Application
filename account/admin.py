from django.contrib import admin
from .models import Profile, Subscription

class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Subscription, SubscriptionAdmin)



