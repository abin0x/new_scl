# payments/urls.py

from django.urls import path
from .views import (
    InitiatePaymentView,
    CompletePaymentView,
    PaymentFailView,
    PaymentCancelView,
    OrderListView
)

urlpatterns = [
    path('initiate-payment/<int:course_id>/', InitiatePaymentView.as_view(), name='initiate-payment'),
    path('complete/', CompletePaymentView.as_view(), name='complete-payment'),
    path('fail/', PaymentFailView.as_view(), name='payment-fail'),
    path('cancel/', PaymentCancelView.as_view(), name='payment-cancel'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    
]
