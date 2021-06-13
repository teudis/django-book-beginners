from django import urls
from django.urls.conf import path

from .views import HomePageView, AboutPageView

urlpatterns  = [
    path('', HomePageView.as_view(), name= 'home'),
    path('about/', AboutPageView.as_view(), name= 'about')
]