from .models import *
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
        fields = (
            'title',
            'excerpt',
            'content',
            'featured_image',
            'categories',
            )
