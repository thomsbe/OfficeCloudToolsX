from django.contrib import admin

from kaffeekasse.models import Purchasing, Attachment, DebtStatus, Debt

admin.site.register(Attachment)
admin.site.register(Purchasing)
admin.site.register(DebtStatus)
admin.site.register(Debt)

