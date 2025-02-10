
from django.urls import path
from .views import *

app_name = 'accounts'





urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/confirm/', LogoutConfirmView.as_view(), name='logout_confirm'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done'),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('profile/edit/', ProfileEditView.as_view(), name="edit_profile"),

    # Password Reset URLs
    path('reset_password/', UserPasswordResetView.as_view() , name='reset_password'),
    path('reset_password/done/', UserPasswordResetDoneView.as_view() , name='password_reset_done'),
    path('confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view() , name='password_reset_confirm'),
    path('confirm/complete/', UserPasswordResetCompleteView.as_view() , name='password_reset_complete'),
  ]
