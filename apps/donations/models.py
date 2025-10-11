from django.db import models

from apps.base.models import BaseModel
from apps.campaigns.models import Campaign


class Donation(BaseModel):
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, blank=True, null=True)
    transaction_id = models.CharField(max_length=255)
    payment_status = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.donor_name



