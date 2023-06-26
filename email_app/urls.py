from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import MainDashboard, EmailCredentialSettingView, UpdateEmailCredentialView, EmailDetailView, MailStatusView, SendEmailView

urlpatterns = [
    path('', login_required(MainDashboard.as_view()), name='main-dashboard'),

    path('set-email-credential', login_required(EmailCredentialSettingView.as_view()), name='set-email-credential'),

    path('update-email-credential', login_required(UpdateEmailCredentialView.as_view()), name='update-email-credential'),

    path('send-email', login_required(SendEmailView.as_view()), name='send-email'),

    path('email-detail/<slug>', login_required(EmailDetailView.as_view()), name='slug'), 

    path('mail-status/<uidb64>', MailStatusView.as_view(), name='mail-status')
]