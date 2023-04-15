from django.urls import path
from .views import Index, AboutUs, Resources


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about-us/', AboutUs.as_view(), name='about-us'),
    path('resources/', Resources.as_view(), name='resources'),
]
