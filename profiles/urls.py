from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/<int:id>/', views.public_profile,
         name='public_profile'),
    path('profile/search/', views.public_profile_search,
         name='public_profile_search'),
    path('profile/list/', views.public_profile_list,
         name='public_profile_list'),
]
