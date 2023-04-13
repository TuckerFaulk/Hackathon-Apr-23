from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request):
    """View for displaying and updating user profile"""
    profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save_m2m()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, template, context)


@login_required
def public_profile(request, id):
    """View for displaying a user's public profile"""
    user_profile = get_object_or_404(UserProfile, id=id)
    public_fields = []
    for field in user_profile._meta.fields:
        if field.name.startswith('is_'):
            if getattr(user_profile, field.name):
                public_fields.append(field.name.replace('is_', ''))

    template = 'profiles/public_profile.html'
    context = {
        'user_profile': user_profile,
        'public_fields': public_fields
    }
    return render(request, template, context)
