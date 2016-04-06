from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Slack(models.Model):
    slack_url = models.CharField('Slack URL', max_length=100, null=False)
    slack_apitoken = models.CharField('Slack Token', max_length=100, null=False)
    slack_apisecret = models.CharField('Slack API Secret', max_length=100, null=False)

    def __str__(self):
        return self.slack_url


class Company(models.Model):
    company_name = models.CharField('Name of the company', max_length=100, null=False, default='Companyname')
    company_logo = models.ImageField('company logo', max_length=255, null=True, blank=True)
    company_text = models.CharField('Some description of the company', max_length=255, null=True, blank=True)
    company_url = models.CharField('A url of the companys homepage', max_length=100, null=True, blank=True)
    company_slack = models.OneToOneField(Slack, null=True,  blank=True)

    def __str__(self):
        return self.company_name


class Office(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    office_name = models.CharField('Name of the office', max_length=100, null=False, default='Officename')

    def __str__(self):
        return self.office_name


class OfficeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    offices = models.ManyToManyField(Office)
    slackid = models.CharField('Slack ID', max_length=100, null=True, blank=True)
    avatar = models.ImageField('avatar img', max_length=255, null=True, blank=True)

    def get_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.user.get_full_name()
