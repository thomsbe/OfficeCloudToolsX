from django.conf.urls import include, url

from kaffeekasse import views

urlpatterns = [
    url(r'^kaffeekasse$', views.kaffeekasse, name="kaffeekasse"),
    url(r'^kaffeekasse/claim_paid/', views.claim_paid, name="claim_paid"),
]