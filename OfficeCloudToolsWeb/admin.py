from django.contrib import admin
from .models import Slack, Company, Office, OfficeUser

admin.site.register(Slack)
admin.site.register(Company)
admin.site.register(Office)
admin.site.register(OfficeUser)

