from . import views
from django.urls import path

urlpatterns = [
    path("post_list/", views.PostList.as_view(), name="post_list"),
]
