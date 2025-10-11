from django.contrib import admin

from apps.donations.models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    pass
