from django.conf.urls import include, url
from django.contrib import admin

from officecloud import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
]