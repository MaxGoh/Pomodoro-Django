from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'home/$', views.home_view, name='home'),
    url(r'profile/$', views.profile_view, name='profile'),
]
