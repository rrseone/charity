# apps/donations/urls.py
from django.urls import path
from .views import DonationCreateView, donation_thank_you_view

app_name = 'donations'

urlpatterns = [
    path('new/', DonationCreateView.as_view(), name='donation_create'), # General donation
    path('new/for/<slug:campaign_slug>/', DonationCreateView.as_view(), name='donation_for_campaign'), # Donate to specific campaign
    path('thank-you/', donation_thank_you_view, name='donation_thank_you'),
]