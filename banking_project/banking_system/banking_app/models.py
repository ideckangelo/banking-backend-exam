from django.db import models
from . import utils
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)

# Create your models here.


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=20, unique=True)
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    # TODO: add format validation on phone_number inputs
    phone_number = models.PositiveIntegerField(max_length=11, blank=False)

    def __str__(self):
        return self.name


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(
        Customer, related_name="accounts", on_delete=models.CASCADE
    )
    # TODO: add formatting for account_number inputs
    account_number = models.PositiveIntegerField(max_length=9, blank=False)
    balance = models.DecimalField(default=0.00, decimal_places=2, max_digits=25)

    def __str__(self):
        return f"{self.account_number:09d}"

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        self.balance -= amount
        self.save()

    def get_balance(self):
        return self.balance

    @classmethod
    def create_account(cls, *args, **kwargs):
        customer_data = kwargs.pop("customer_id")
        customer, created = Customer.objects.get_or_create(**customer_data)
        account = cls(customer_id=customer, **kwargs)
        account.save()
        return account

    @classmethod
    def save_account(cls, *args, **kwargs):
        customer_data = kwargs.pop("customer_id")
        customer = Customer.objects.filter(customer_id=customer_data["customer_id"])
        customer.update(**customer_data)
        customer_inst = Customer.objects.get(customer_id=customer_data["customer_id"])
        account = cls(customer_id=customer_inst, **kwargs)
        return account


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(
        Account, related_name="transactions", on_delete=models.CASCADE
    )
    amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=25)
    transaction_type = models.CharField(
        choices=utils.TRANSACTION_TYPES, blank=False, max_length=10
    )

    def __str__(self):
        return str(self.transaction_id)

    def digest_transaction(self):
        if self.transaction_type == utils.DEPOSIT:
            self.account_id.deposit(amount=self.amount)
        elif self.transaction_type == utils.WITHDRAW:
            if self.amount > self.account_id.get_balance():
                raise ValueError(
                    "You are withdrawing more than your available account balance. Please try again."
                )
            else:
                self.account_id.withdraw(amount=self.amount)

    @classmethod
    def make_transaction(cls, *args, **kwargs):
        # TODO: improve as this is essentially a duplicate of cls.save
        transaction = cls(**kwargs)
        transaction.save()
        return transaction

    def save(self, *args, **kwargs):
        self.digest_transaction()
        super().save(*args, **kwargs)
