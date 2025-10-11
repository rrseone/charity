from django.views.generic import ListView, DetailView
from taggit.models import Tag

from apps.blog.models import Post, Category
from apps.campaigns.models import Campaign


class CampaignListView(ListView):
    model = Campaign
    template_name = 'pages/campaigns/campaign_list.html'
    context_object_name = 'campaigns'
    queryset = Campaign.objects.active().order_by('-created_at')
    paginate_by = 6

    def get_queryset(self):
        return Campaign.objects.active().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_title'] = "All Campaigns"
        return context

class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'pages/campaigns/campaign_detail.html'
    context_object_name = 'campaign'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_title'] = self.object.title
        context['recent_posts'] = Post.objects.filter(status='published').order_by('-published_date')[:4]
        context['categories'] = Category.objects.active()
        context['tags'] = Tag.objects.all()
        return context