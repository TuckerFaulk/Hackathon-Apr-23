from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/<int:id>/', views.public_profile,
         name='public_profile'),
]
