from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import BankAccount
from .forms import BankForm


def account_list(request):
    accounts = BankAccount.objects.all()
    return render(request, 'accounts/account_list.html', {'accounts': accounts})


def save_account_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            accounts = BankAccount.objects.all()
            data['html_account_list'] = render_to_string('accounts/includes/partial_account_list.html', {
                'accounts': accounts
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def account_create(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
    else:
        form = BankForm()
    return save_account_form(request, form, 'accounts/includes/partial_account_create.html')


def account_update(request, pk):
    account = get_object_or_404(BankAccount, pk=pk)
    if request.method == 'POST':
        form = BankForm(request.POST, instance=account)
    else:
        form = BankForm(instance=account)
    return save_account_form(request, form, 'accounts/includes/partial_account_update.html')


def account_delete(request, pk):
    account = get_object_or_404(BankAccount, pk=pk)
    data = dict()
    if request.method == 'POST':
        account.delete()
        data['form_is_valid'] = True
        accounts = BankAccount.objects.all()
        data['html_account_list'] = render_to_string('accounts/includes/partial_account_list.html', {
            'accounts': accounts
        })
    else:
        context = {'account': account}
        data['html_form'] = render_to_string('accounts/includes/partial_account_delete.html', context, request=request)
    return JsonResponse(data)
