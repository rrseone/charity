from django.views.generic import ListView, DetailView

from apps.services.models import Service


class ServiceListView(ListView):
    model = Service
    template_name = 'pages/services/service_list.html'
    context_object_name = 'services'
    paginate_by = 10

    def get_queryset(self):
        return Service.objects.active()


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'pages/services/event_detail.html'
    context_object_name = 'service'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Service.objects.active()
