from . import views
from django.urls import path

urlpatterns = [
    path("post_list/", views.PostList.as_view(), name="post_list"),
    path("<slug:slug>", views.PostDetail.as_view(), name="post_detail"),
    path("like/<slug:slug>", views.PostLike.as_view(), name="post_like")
]
