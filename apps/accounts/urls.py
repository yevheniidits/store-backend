from django.urls import path

from apps.accounts.views.password_reset import PasswordResetRequestView, PasswordResetConfirmView

app_name = 'accounts'

urlpatterns = [
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]
