from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'recipient', 'timestamp', 'read',)
    list_filter = ('read',)
    search_fields = ('subject', 'sender__username', 'recipient__username',)
