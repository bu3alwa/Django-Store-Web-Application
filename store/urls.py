from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('contact', views.contact, name='contact'),
    path('terms-of-service', views.terms, name='terms'),
]
