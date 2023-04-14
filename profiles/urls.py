from django.urls import path
from . import views
from django.conf import settings
from .views import FollowList, public_profile


urlpatterns = [
     path('profile/', views.profile, name='profile'),
     path('profile/<int:id>/', views.public_profile,
          name='public_profile'),
     path('profile/search/', views.public_profile_search,
          name='public_profile_search'),
     path('profile/list/', views.public_profile_list,
          name='public_profile_list'),
     path('add-to-follow-list/<int:user_id>/',
          views.add_to_follow, name='add_to_follow'),
     path('profile/unfollow/<int:follow_id>/', views.remove_from_follow_list,
          name='remove_from_follow_list'),
]
