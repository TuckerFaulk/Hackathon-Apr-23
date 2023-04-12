from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).orderby("-created_on")
    template_name = "post_list.html"
    paginate_by = 24
