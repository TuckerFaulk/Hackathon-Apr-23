from django.contrib import admin
from .models import Author, Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Author)
class AuthorAdmin(SummernoteModelAdmin):
    list_display = ('user',)
    search_fields = ['user']
    list_filter = ('user',)


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'subtitle')
    search_fields = ['title', 'subtitle']
    list_filter = ('title', 'subtitle')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    summernote_fields = ('body')
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
