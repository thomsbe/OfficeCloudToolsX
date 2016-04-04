from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Slack(models.Model):
    slack_url = models.CharField('Slack URL', max_length=100)
    slack_apitoken = models.CharField('Slack Token', max_length=100)
    slack_apisecret = models.CharField('Slack API Secret', max_length=100)


class Company(models.Model):
    company_name = models.CharField('Name of the company', max_length=100)
    company_logo = models.CharField('URL of the company logo', max_length=255)
    company_text = models.CharField('Some description of the company', max_length=255)
    company_url = models.CharField('A url of the companys homepage', max_length=100)
    company_slack = models.OneToOneField(Slack)


class Office(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    office_name = models.CharField('Name of the office', max_length=100)


class OfficeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    offices = models.ManyToManyField(Office)
    slackid = models.CharField('Slack ID', max_length=100)
