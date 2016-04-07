from django.shortcuts import render
from django.http import JsonResponse

from kaffeekasse.models import *
from .forms import PurchasingForm

# Create your views here.
def kaffeekasse(request):
    # get debts
    all_debts = Debt.objects.all().filter(debt_payer=request.user.officeuser)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PurchasingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            attachment = Attachment(attachment_filename=request.FILES['purchasing_attachment'])
            attachment.attachment_name = form.cleaned_data['purchasing_attachment_name']
            attachment.save()

            purchase = Purchasing()
            purchase.purchasing_name = form.cleaned_data['purchasing_name']
            purchase.purchasing_date = form.cleaned_data['purchasing_date']
            purchase.purchasing_value = form.cleaned_data['purchasing_value']
            purchase.purchasing_user = request.user.officeuser
            purchase.purchasing_attachment = attachment
            purchase.save()

            payer = OfficeUser.objects.get(id=form.cleaned_data['debtor_name'])
            status = DebtStatus.objects.get(status_ident='open')

            debt = Debt()
            debt.debt_purchasing = purchase
            debt.debt_creditor = request.user.officeuser
            debt.debt_payer = payer
            debt.debt_value = form.cleaned_data['debt_amount']
            debt.debt_status = status
            debt.save()

            debt_count = form.cleaned_data['debt_count']
            for i in range(1, int(debt_count)+1):
                payer = OfficeUser.objects.get(id=request.POST['debtor_name'+str(i)])

                debt = Debt()
                debt.debt_purchasing = purchase
                debt.debt_creditor = request.user.officeuser
                debt.debt_payer = payer
                debt.debt_value = request.POST['debt_amount'+str(i)]
                debt.debt_status = status
                debt.save()

            # get all claims
            all_claims = Debt.objects.all().filter(debt_creditor=request.user.officeuser)

            # redirect to a new URL:
            return render(request, 'kaffeekasse.html', {'form' : form, 'success' : True, 'debts': all_debts, 'claims': all_claims})
    # if a GET (or any other method) we'll create a blank form
    else:
        # get all claims
        all_claims = Debt.objects.all().filter(debt_creditor=request.user.officeuser)
        form = PurchasingForm()
    return render(request, 'kaffeekasse.html', {'form' : form, 'success' : False, 'debts': all_debts, 'claims': all_claims})

def claim_paid(request):
    id = request.POST['id']
    claim = Debt.objects.get(pk=id)

    # check if user who sent request is creditor
    if claim.debt_creditor != request.user.officeuser:
        msg = 'Fehler: falscher Benutzer'
        success = False
    else:
        status = DebtStatus.objects.get(status_ident='closed')
        claim.debt_status = status
        claim.save()
        msg = 'Forderung geschlossen'
        success = True

    response_data = {}
    response_data['msg'] = msg
    response_data['id'] = id
    response_data['success'] = success

    return JsonResponse(response_data)