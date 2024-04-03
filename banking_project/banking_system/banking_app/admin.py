from django.contrib import admin
from . import models

# Register your models here.


class AccountInline(admin.TabularInline):
    model = models.Account
    readonly_fields = ["account_id", "account_number", "balance"]
    extra = 0


class TransactionInline(admin.TabularInline):
    model = models.Transaction
    readonly_fields = ["transaction_id", "amount", "transaction_type"]
    extra = 0


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["customer_id", "name", "email", "phone_number"]
    list_display_links = ["name"]
    inlines = [AccountInline]


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["account_id", "customer_id", "account_number", "balance"]
    list_display_links = ["customer_id"]
    inlines = [TransactionInline]


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["transaction_id", "account_id", "amount", "transaction_type"]
    list_display_links = ["transaction_id"]
