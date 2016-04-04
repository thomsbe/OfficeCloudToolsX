from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from officecloud.models import OfficeUser


class Attachment(models.Model):
    attachment_name = models.CharField('Name of the attachment', max_length=255)
    attachment_filename = models.CharField('Path of the attachment', max_length=255)
    attachment_date = models.DateField()


class Purchasing(models.Model):
    purchasing_name = models.CharField(max_length=100)
    purchasing_date = models.DateField()
    purchasing_value = models.FloatField()


class DebtStatus(models.Model):
    status_name = models.CharField(max_length=20)
    status_desc = models.CharField(max_length=255)


class Debt(models.Model):
    debt_creditor = models.ForeignKey(OfficeUser, related_name='debitor')
    debt_payer = models.ForeignKey(OfficeUser, related_name='creditor')
    debt_value = models.FloatField('Value of this debt')
    debt_status = models.ForeignKey(DebtStatus)
