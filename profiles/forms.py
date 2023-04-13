from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    is_preferred_display_name = forms.BooleanField(required=False)
    is_fullname = forms.BooleanField(required=False)
    is_user_email = forms.BooleanField(required=False)
    is_user_phone = forms.BooleanField(required=False)
    is_linkedin = forms.BooleanField(required=False)
    is_profile_picture = forms.BooleanField(required=False)
    is_about_me = forms.BooleanField(required=False)
    is_rank = forms.BooleanField(required=False)
    is_branch_of_military_served = forms.BooleanField(required=False)
    is_length_of_service = forms.BooleanField(required=False)
    is_past_deployments = forms.BooleanField(required=False)

    class Meta:
        model = UserProfile
        fields = [
            'preferred_display_name',
            'slug',
            'fullname',
            'user_email',
            'user_phone',
            'linkedin',
            'profile_picture',
            'about_me',
            'rank',
            'branch_of_military_served',
            'length_of_service',
            'past_deployments',
        ]

    def save(self, commit=True):
        # Get the cleaned data once to avoid repeated lookups
        cleaned_data = self.cleaned_data

        instance = super().save(commit=False)

        # Set the flags based on the checkbox values
        instance.is_preferred_display_name = cleaned_data.get('is_preferred_display_name', False)
        instance.is_fullname = cleaned_data.get('is_fullname', False)
        instance.is_user_email = cleaned_data.get('is_user_email', False)
        instance.is_user_phone = cleaned_data.get('is_user_phone', False)
        instance.is_linkedin = cleaned_data.get('is_linkedin', False)
        instance.is_profile_picture = cleaned_data.get('is_profile_picture', False)
        instance.is_about_me = cleaned_data.get('is_about_me', False)
        instance.is_rank = cleaned_data.get('is_rank', False)
        instance.is_branch_of_military_served = cleaned_data.get('is_branch_of_military_served', False)
        instance.is_length_of_service = cleaned_data.get('is_length_of_service', False)
        instance.is_past_deployments = cleaned_data.get('is_past_deployments', False)

        if commit:
            instance.save()

        return instance
