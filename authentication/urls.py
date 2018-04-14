from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm


urlpatterns = [

    re_path(r'^login/$', auth_views.LoginView.as_view(
        template_name='authentication/login.html',
        form_class=LoginForm), 
        name='login'),

    re_path(r'^logout/$', auth_views.LogoutView.as_view(
        template_name='authentication/logout.html')
        , name='logout'),

    re_path(r'^register/$', views.register_view, name='register'),
]
