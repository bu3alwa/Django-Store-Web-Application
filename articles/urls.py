from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'(?P<slug>[-w]+)/$', views.post_detail, name='post-detail'),
]
