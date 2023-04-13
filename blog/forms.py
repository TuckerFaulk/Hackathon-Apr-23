from .models import Author, Category, Post, Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta():
        model: Comment
        fields = (
            'body',
            )


class PostForm(forms.ModelForm):
    class Meta():
        model: Post
        fields = (
            'title',
            'except',
            'content',
            'featured_image',
            'categories',
            )
