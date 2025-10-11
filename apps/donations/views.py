from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



from apps.donations.models import Donation
from apps.campaigns.models import Campaign
from django.shortcuts import get_object_or_404, render
from apps.donations.forms import DonationForm


class DonationCreateView(CreateView):
    model = Donation
    form_class = DonationForm
    fields = ['donor_name', 'donor_email', 'amount', 'campaign', 'is_anonymous']
    template_name = 'pages/donations/donation_form.html'
    success_url = reverse_lazy('donations:donation_thank_you')

    def form_valid(self, form):
        campaign_id = self.request.POST.get('campaign_id') or self.request.GET.get('campaign_id')
        if campaign_id:
            form.instance.campaign = get_object_or_404(Campaign, pk=campaign_id)

        response = super().form_valid(form)

        if form.instance.campaign and form.instance.payment_status == 'successful':
            campaign = form.instance.campaign
            campaign.raised += form.instance.amount
            campaign.save()
        return response

    def get_initial(self):
        initial = super().get_initial()
        campaign_slug = self.kwargs.get('campaign_slug')
        if campaign_slug:
            campaign = get_object_or_404(Campaign, slug=campaign_slug)
            initial['campaign'] = campaign
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        campaign_slug = self.kwargs.get('campaign_slug')
        if campaign_slug:
            context['campaign_to_donate'] = get_object_or_404(Campaign, slug=campaign_slug)
        return context

def donation_thank_you_view(request):
    return render(request, 'pages/donations/donation_thank_you.html')
