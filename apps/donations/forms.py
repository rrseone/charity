# apps/donations/forms.py
from django import forms
from .models import Donation
from apps.campaigns.models import Campaign


class DonationForm(forms.ModelForm):
    # Add a hidden field or a non-model field for campaign_id if needed
    # campaign_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Donation
        fields = ['donor_name', 'donor_email', 'amount', 'campaign', 'is_anonymous']
        widgets = {
            'campaign': forms.Select(attrs={'class': 'form-control'}),  # Example
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally, filter campaign choices or set a default
        # self.fields['campaign'].queryset = Campaign.objects.filter(is_active=True)