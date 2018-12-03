from django import forms

from .models import BankAccount


class BankForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ('number', 'balance', 'account_type', 'owner_full_name', 'owner_birth_date')
