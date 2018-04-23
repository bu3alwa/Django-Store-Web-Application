from django.conf import settings

def global_settings(request):
    return {
            'GOOGLE_ANALYTICS': settings.GOOGLE_ANALYTICS,
            'ZENDESK': settings.ZENDESK,
            }

