from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('billing/', views.billing, name='billing'),
    path('billing/cancel', views.cancel, name='cancel'),
]
