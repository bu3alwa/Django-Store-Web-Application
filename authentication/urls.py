from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='authentication/login.html',
        form_class=LoginForm), 
        name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        template_name='authentication/logout.html')
        , name='logout'),

    path('register/', views.register_view, name='register'),
    path('register_success/', views.register_success, name='register_success'),
]
