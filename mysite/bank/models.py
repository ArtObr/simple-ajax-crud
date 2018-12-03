from __future__ import unicode_literals

from django.db import models


class BankAccount(models.Model):
    CHECKING = 1
    SAVINGS = 2
    ACCOUNT_TYPES = (
        (CHECKING, 'Checking'),
        (SAVINGS, 'Savings'),
    )
    number = models.CharField(max_length=20, unique=True)
    balance = models.IntegerField()
    account_type = models.PositiveSmallIntegerField(choices=ACCOUNT_TYPES)
    owner_full_name = models.CharField(max_length=300)
    owner_birth_date = models.DateField()
