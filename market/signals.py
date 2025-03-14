from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added, social_account_updated
from allauth.account.signals import user_signed_up
from django.shortcuts import redirect
from django.contrib import messages

@receiver(social_account_added)
def social_account_added_handler(request, sociallogin, **kwargs):
    """Handle when a social account is added to an existing account"""
    messages.success(request, f'Successfully connected {sociallogin.account.provider} account.')

@receiver(user_signed_up)
def social_signup_handler(request, user, **kwargs):
    """Handle new user signup through social account"""
    messages.success(request, f'Welcome to DG TWIN MARKET! Your account has been created successfully.')

@receiver(social_account_updated)
def social_account_updated_handler(request, sociallogin, **kwargs):
    """Handle when a social account is updated"""
    messages.info(request, f'Your {sociallogin.account.provider} account information has been updated.') 