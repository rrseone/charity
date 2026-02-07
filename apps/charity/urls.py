from django.urls import path

from apps.charity.views import HomePageView, AboutPageView, DetailPageView

app_name = 'charity'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about-us/', AboutPageView.as_view(), name='about_us'),
]