from django.conf.urls import include, url

from kaffeekasse import views

urlpatterns = [
    url(r'^/kaffeekasse', views.kaffeekasse, name="kaffeekasse"),
]