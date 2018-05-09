from django.urls import path
from . import views

urlpatterns = [
    path('gotap', views.gotap_process, name='gotap process'),
    path('knet', views.KnetProcess.as_view(), name='knet process'),
]
