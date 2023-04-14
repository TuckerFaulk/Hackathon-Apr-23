from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserProfileForm
from .models import UserProfile, FollowList
from django.db.models import Q
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_POST


@login_required
def profile(request):
    """View for displaying and updating user profile"""
    profile = request.user.userprofile
    followed_users = (
        FollowList.objects.filter(user=request.user).select_related('followed_user')
    )
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
        'followed_users': followed_users,
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

    current_user_profile = request.user.userprofile

    template = 'profiles/public_profile.html'
    context = {
        'user_profile': user_profile,
        'public_fields': public_fields,
        'current_user_profile': current_user_profile,
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


def followlist(request):
    """ A view to show the user's followlist """
    if not request.user.is_authenticated:
        messages.error(
            request,
            'Sorry, you need to be logged in to add your FollowList.'
        )
        return redirect(reverse('account_login'))

    user = request.user
    followed_users = (
        FollowList.objects.filter(user=user).select_related('followed_user')
    )
    context = {
        'followed_users': followed_users,
    }
    return render(request, 'profile.html', context)


def add_to_follow(request, user_id):
    """
    A view to add other users to a user's follow list and prevent users from
    adding users that are already in their follow list.
    """
    if not request.user.is_authenticated:
        messages.error(
            request,
            'Sorry, you need to be logged in to follow other users.'
        )
        return redirect(reverse('account_login'))

    user = get_object_or_404(User, id=user_id)
    followed_user = get_object_or_404(UserProfile, user=user)

    # Check if the user is already in the follow list
    existing = FollowList.objects.filter(followed_user=followed_user,
                                         user=request.user).exists()

    if existing:
        messages.info(
            request,
            f'{followed_user.preferred_display_name} is already in your list.'
        )
    else:
        follow_user = FollowList.objects.create(followed_user=followed_user,
                                                user=request.user)
        messages.success(
            request,
            f'{followed_user.preferred_display_name} is added to your list.'
        )

    return redirect(reverse('public_profile', args=[followed_user.id]))


def remove_from_follow_list(request, user_id):
    """ A view to remove public_profile from followlist """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to add your List.')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, user=request.user)
    public_profile = get_object_or_404(UserProfile, pk=UserProfile.id)
    FollowList.objects.filter(UserProfile=UserProfile,
                              user_profile=user).delete()
    messages.info(
        request,
        f'{user_profile.preferred_display_name} was removed from your Wishlist'
    )

    return redirect(reverse('public_profile', args=[public_profile.id]))
