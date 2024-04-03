from rest_framework import viewsets, status
from . import serializers, models
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
# TODO: Add permissions to the ModelViewSets


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AccountSerializer
    queryset = models.Account.objects.all()

    @action(
        detail=False,
        methods=["get"],
        url_path="find-account-by-customer/(?P<customer_id>\d+)",
    )
    def find_account_by_customer(self, request, customer_id=None):
        try:
            account = models.Account.objects.get(customer_id=customer_id)
            serializer = self.get_serializer(account)
            return Response(serializer.data)
        except:
            return Response(
                {"message": "Account not found for customer_id {}".format(customer_id)},
                status=status.HTTP_404_NOT_FOUND,
            )


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransactionSerializer
    queryset = models.Transaction.objects.all()

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed("Update method is not allowed for transactions.")

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("Partial update method is not allowed for transactions.")


class StatementViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StatementSerializer
    queryset = models.Account.objects.all()
