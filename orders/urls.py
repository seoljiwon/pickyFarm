from django.urls import path, include
from . import views


app_name = "orders"

urlpatterns = [
    path("orderingCart/", views.orderingCart, name="ordering_cart"),
    path("payment/update/<int:pk>/", views.payment_update, name="payment_update"),
    path("payment/", views.payment_create, name="payment_create"),
    # path('payment/success', views.payment_success, name="payment_success"),
    path("payment/fail", views.payment_fail, name="payment_fail"),
    path("payment/valid", views.payment_valid, name="payment_valid"),
    path("payment/cancel/<int:pk>", views.order_cancel, name="payment_cancel"),
    # path('payment_fail', views.fail_test, name="fail_test"), 결제취소 창 테스트용 path
    path("change-refund/", views.create_change_or_refund, name="change_refund")
]
