from django.urls import path
from .views import RegisterView, LogoutAPIView, SetNewPasswordAPIView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, \
    RequestPasswordResetEmail, DeleteAccount  # RegisterView_for_mobile
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('admin/register', RegisterView.as_view(), name="register"),
    #path('register/MobileUser', RegisterView_for_mobile.as_view(), name="register"),
    path('admin/login', LoginAPIView.as_view(), name="login"),
    path('admin/logout', LogoutAPIView.as_view(), name="logout"),
    path('admin/email-verify', VerifyEmail.as_view(), name="email-verify"),
    path('admin/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/<int:id>', DeleteAccount.as_view(), name="delete"),

    # path('request-reset-email/', RequestPasswordResetEmail.as_view(),
   #      name="request-reset-email"),
   # path('password-reset/<uidb64>/<token>/',
    #     PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
   # path('password-reset-complete', SetNewPasswordAPIView.as_view(),
    #     name='password-reset-complete'),

]
