from rest_framework import serializers
from . import models
from random import randrange


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ["customer_id", "name", "email", "phone_number"]


class AccountSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(source="customer_id.customer_id")
    name = serializers.CharField(source="customer_id.name")
    email = serializers.EmailField(source="customer_id.email")
    phone_number = serializers.IntegerField(source="customer_id.phone_number")

    # auto-generated attributes
    account_number = serializers.IntegerField(required=False, read_only=True)
    balance = serializers.DecimalField(
        required=False, decimal_places=2, max_digits=25, read_only=True
    )

    class Meta:
        model = models.Account
        fields = [
            "customer_id",
            "name",
            "email",
            "phone_number",
            "account_id",
            "account_number",
            "balance",
        ]

    def create(self, validated_data):
        # TODO: add formatting for account_number inputs
        validated_data["account_number"] = randrange(0, 999999999)
        account = models.Account.create_account(**validated_data)
        return account

    def update(self, instance, validated_data):
        instance = instance.save_account(**validated_data)
        return instance


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = ["transaction_id", "account_id", "amount", "transaction_type"]

    def create(self, validated_data):
        transaction = models.Transaction.make_transaction(**validated_data)
        return transaction


class StatementSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Account
        fields = ["account_id", "account_number", "balance", "transactions"]
        read_only_fields = ["account_id", "account_number", "balance", "transactions"]
