from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"accounts", views.AccountViewSet, basename="account")
router.register(r"transactions", views.TransactionViewSet, basename="transaction")
router.register(r"statements", views.StatementViewSet, basename="statement")

urlpatterns = [
    path("", include(router.urls)),
]
