from django.urls import path

from apps.charity.views import HomePageView, AboutPageView, DetailPageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-detail'),
    path('about-us/', AboutPageView.as_view(), name='about_us-detail'),
    path('pages/<slug:slug>/', DetailPageView.as_view(), name='page_detail'),
]