from django import forms
from material import *

from officecloud.models import OfficeUser


class PurchasingForm(forms.Form):
    all_users = OfficeUser.objects.all()
    user_choices = []
    for user in all_users:
        user_choices.append((user.id, user.get_name()))

    purchasing_name = forms.CharField(label='Name', max_length=100)
    purchasing_value = forms.FloatField(label='Einkaufswert')
    purchasing_date = forms.DateField(label='Enkaufsdatum')
    purchasing_attachment_name = forms.CharField(label='Kassenscheinbezeichnung', max_length=255)
    purchasing_attachment = forms.ImageField(label='Kassenschein', required=False)
    debtor_name = forms.ChoiceField(label='Schuldner', choices=user_choices)
    debt_amount = forms.FloatField(label='Summe')
    debt_count = forms.IntegerField(required = False)

    layout = Layout(
        'purchasing_name',
        'purchasing_value',
        'purchasing_date',
        'purchasing_attachment_name',
        'purchasing_attachment',
        Fieldset('Kostenverteilung',
                 Row(Span6('debtor_name'), Span6('debt_amount'))),
        'debt_count'
    )