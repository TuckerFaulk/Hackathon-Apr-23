from .models import *
from profiles.models import UserProfile
from django import forms


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = (
            'body',
            )


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        readonly_fields = 'author'
        fields = (
            'title',
            'excerpt',
            'content',
            'featured_image',
            'categories',
            )
