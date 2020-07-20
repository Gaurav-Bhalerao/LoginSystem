from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('profile/',views.profile,name="profile"),
    path('user_profile_update/',views.user_profile_update,name="user_profile_update"),
    path('login_handel/',views.login_handel,name="login"),
    path('logout_handel/',views.logout_handel,name="logout"),
    path('error/',views.error,name="error"),
    # For Password Reset
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]
