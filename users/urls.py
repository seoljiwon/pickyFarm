from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("login/kakao/", views.kakao_login, name="kakao_login"),
    path("login/kakao/callback", views.kakao_callback, name="kakao_login_callback"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path(
        "signup/terms_of_service",
        views.terms_of_service_popup,
        name="signup_terms_of_service",
    ),
    path("signup/personal_info", views.personal_info_popup, name="signup_personal_info"),
    path("signup/id_validation/", views.idValidation, name="id_validation"),
    path(
        "signup/nickname_validation/",
        views.nicknameValidation,
        name="nickname_validation",
    ),
    path("signup/email_validation/", views.emailValidation, name="email_validation"),
    path(
        "signup/phone_number_validation/",
        views.phoneNumberValidation,
        name="phone_number_validation",
    ),
    path(
        "signup/phone_number_authentication/",
        views.phoneNumberAuthentication,
        name="phone_number_authentication",
    ),
    path("password_reset/", views.MyPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.MyPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset/<uidb64>/<token>/",
        views.MyPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.MyPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("mypage/<slug:cat>", views.mypage, name="mypage"),
    path("editor_mypage/", views.EditorMyPage.as_view(), name="editor_mypage"),
    path(
        "editor_mypage/comments",
        views.EditorMyPage_Comments.as_view(),
        name="editor_mypage_comments",
    ),
    path(
        "editor_mypage/info",
        views.EditorMypage_Info.as_view(),
        name="editor_mypage_info",
    ),
    path("find_my_id/", views.FindMyIdView.as_view(), name="find_my_id"),
    path("find_my_id/complete", views.FindMyIdView.as_view(), name="find_my_id_complete"),
    path("find_my_id/failed", views.FindMyIdFailView.as_view(), name="find_my_id_failed"),
    path("cartIn/", views.CartInAjax, name="cartInAjax"),
    path("cartOut/", views.cartOutAjax, name="cartOutAjax"),
    path("subs/", views.subs, name="subs"),
    path("cancelSubs/", views.cancelSubs, name="cancelSubs"),
    path("wish/", views.wish, name="wish"),
    path("cancelWish/", views.cancelWish, name="cancelWish"),
    path("infoUpdate/", views.infoUpdate, name="infoUpdate"),
    path("profileUpdate/", views.profileUpdate, name="profileUpdate"),
    path("test/", views.testview, name="testview"),
    path("reviewtest/", views.reviewtest, name="reviewtest"),
    path("product_refund_test/", views.product_refund, name="product_refund"),
    # mypage popups
    path(
        "mypage/orders/cancel/<int:pk>",
        views.OrderCancelPopup.as_view(),
        name="mypage_order_cancel_popup",
    ),
]
