from django.utils import timezone
from django.views.generic import TemplateView

from apps.charity.models import Member
from apps.campaigns.models import Campaign
from apps.events.models import Event
from apps.blog.models import Post

from django.contrib.auth import get_user_model

from apps.services.models import Service

User = get_user_model()


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_services'] = Service.objects.active().order_by('-is_featured', '-created_at')[:3]
        context['featured_campaigns'] = Campaign.objects.active().filter(end_date__lt=timezone.now()).order_by('-start_date')[:3]
        context['featured_events'] = Event.objects.filter().order_by('event_date', '-event_start_time')[:3]
        context['featured_members'] = Member.objects.active().filter().order_by('-is_featured', '-created_at')[:4]
        context['featured_staffs'] = User.objects.filter(is_staff=True).order_by('-is_featured', '-created_at')[:5]
        context['featured_posts'] = Post.objects.active().filter(status='published').order_by('-is_featured', '-published_date')[:2]
        return context


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['team_members'] = TeamMember.objects.all()
        return context

class DetailPageView(TemplateView):
    template_name = "pages/page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['name'] = "Title"
        return context

