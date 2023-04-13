from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile
from django.db.models import Q


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


def public_profile_list(request):
    queryset = UserProfile.objects.filter(is_preferred_display_name=True)
    rank = request.GET.get('rank')
    branch_of_military_served = request.GET.get('branch_of_military_served')
    length_of_service = request.GET.get('length_of_service')
    past_deployments = request.GET.get('past_deployments')

    if rank:
        queryset = queryset.filter(rank__icontains=rank)
    if branch_of_military_served:
        queryset = queryset.filter(
            branch_of_military_served__icontains=branch_of_military_served
        )
    if length_of_service:
        queryset = queryset.filter(
            length_of_service__icontains=length_of_service
        )
    if past_deployments:
        queryset = queryset.filter(
            Q(past_deployments__icontains=past_deployments)
        )

    context = {
        'queryset': queryset,
        'rank': rank,
        'branch_of_military_served': branch_of_military_served,
        'length_of_service': length_of_service,
        'past_deployments': past_deployments,
    }
    return render(request, 'profiles/public_profile_list.html', context)


def public_profile_search(request):
    search_term = request.GET.get('q')
    rank = request.GET.get('rank')
    branch_of_military_served = request.GET.get('branch_of_military_served')
    length_of_service = request.GET.get('length_of_service')
    deployment = request.GET.get('deployment')

    profiles = UserProfile.objects.all()

    if search_term:
        profiles = profiles.filter(user__username__icontains=search_term)

    if rank:
        profiles = profiles.filter(rank=rank)

    if branch_of_military_served:
        profiles = profiles.filter(
            branch_of_military_served=branch_of_military_served
        )

    if length_of_service:
        profiles = profiles.filter(
            length_of_service__icontains=length_of_service
        )

    if deployment:
        profiles = profiles.filter(deployment__icontains=deployment)

    context = {
        'profiles': profiles,
        'search_term': search_term,
        'rank': rank,
        'branch_of_military_served': branch_of_military_served,
        'length_of_service': length_of_service,
        'deployment': deployment,
    }

    return render(request, 'profiles/public_profile_list.html', context)
