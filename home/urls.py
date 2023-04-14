from django.urls import path
from .views import Index, AboutUs


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about-us/', AboutUs.as_view(), name='about-us'),
]
