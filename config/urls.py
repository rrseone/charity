from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.pages.urls', namespace='pages')),
    path('services/', include('apps.services.urls', namespace='services')),
    path('campaigns/', include('apps.campaigns.urls', namespace='campaigns')),
    path('events/', include('apps.events.urls', namespace='events')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('contact/', include('apps.contacts.urls', namespace='contact')),
    path('donations/', include('apps.donations.urls', namespace='donations')),
    path('editorjs/', include('django_editorjs_fields.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)