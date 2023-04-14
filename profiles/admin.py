from django.contrib import admin
from .models import UserProfile, FollowList


class UserProfileAdmin(admin.ModelAdmin):
    """Define the admin model for UserProfile"""
    list_display = ('preferred_display_name', 'user_email', 'user_phone',
                    'branch_of_military_served')
    list_filter = ('branch_of_military_served',)
    search_fields = ('preferred_display_name', 'user_email', 'user_phone')


class FollowListAdmin(admin.ModelAdmin):
    """"Define the admin model for the FollowList"""
    list_display = ('user', 'followed_user')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FollowList, FollowListAdmin)
