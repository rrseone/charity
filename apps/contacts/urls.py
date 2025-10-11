from django.urls import path
from .views import ContactCreateView, contact_success_view

app_name = 'contact'

urlpatterns = [
    path('', ContactCreateView.as_view(), name='contact_create'),
    path('success/', contact_success_view, name='contact_success'),
]