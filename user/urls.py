from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    # path('login/', LoginView.as_view(template_name='user/login.html', redirect_authenticated_user=True),
    # name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path("password-reset/", PasswordResetView.as_view(template_name='user/password_reset.html'),
         name="password_reset"),
    path("password-reset/done/", PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path("password-reset-complete/",
         PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name="password_reset_complete"),
    path('resendOTP/', views.resend_otp),
    path('followers', views.followers),
    path('following', views.following),
    path('notifications', views.notifications),
    path('notifications/clear', views.clear_notifications),
    path('islogin', views.islogin),
    path('<str:username>', views.profile, name='profile'),
    path('change/<str:fieldname>', views.ChangeIntoProfile),
]
