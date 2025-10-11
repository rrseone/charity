from django.views.generic import ListView, DetailView
from taggit.models import Tag

from apps.blog.models import Post, Category
from apps.events.models import Event


class EventListView(ListView):
    model = Event
    template_name = 'pages/events/event_list.html'
    context_object_name = 'events'
    paginate_by = 5

    def get_queryset(self):
        return Event.objects.active().order_by('-event_date', '-event_start_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_title'] = 'All Events'
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'pages/events/event_detail.html'
    context_object_name = 'event'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False, is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_title'] = self.object.title
        context['recent_posts'] = Post.objects.filter(status='published').order_by('-published_date')[:4]
        context['categories'] = Category.objects.active()
        context['tags'] = Tag.objects.all()
        return context
