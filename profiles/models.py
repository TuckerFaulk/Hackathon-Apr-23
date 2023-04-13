from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from djrichtextfield.models import RichTextField
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save


# Choice fields
BRANCH_OF_MILITARY = (
    ('british_army', 'British Army'),
    ('royal_air_force', 'Royal Air Force'),
    ('royal_marines', 'Royal Marines'),
    ('royal_navy', 'Royal Navy'),
)


class UserProfile(models.Model):
    """ A model to create and manage User Profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='userprofile')
    preferred_display_name = models.CharField(max_length=50, null=False,
                                              blank=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    user_email = models.EmailField(max_length=100, null=True, blank=True)
    user_phone = models.CharField(max_length=20, null=True, blank=True)
    linkedin = models.CharField(max_length=250, null=True, blank=True)
    profile_picture = CloudinaryField('image', default='placeholder')
    about_me = RichTextField(max_length=1000, null=True, blank=True)
    rank = models.CharField(max_length=200, null=True, blank=True)
    branch_of_military_served = models.CharField(max_length=100,
                                                 choices=BRANCH_OF_MILITARY,
                                                 default='british_army')
    length_of_service = models.IntegerField(null=True, blank=True)
    past_deployments = RichTextField(max_length=300, null=True, blank=True)

    # Boolean fields to indicate whether each field should be public or private
    is_preferred_display_name = models.BooleanField(default=False)
    is_fullname = models.BooleanField(default=False)
    is_user_email = models.BooleanField(default=False)
    is_user_phone = models.BooleanField(default=False)
    is_linkedin = models.BooleanField(default=False)
    is_profile_picture = models.BooleanField(default=False)
    is_about_me = models.BooleanField(default=False)
    is_rank = models.BooleanField(default=False)
    is_branch_of_military_served = models.BooleanField(default=False)
    is_length_of_service = models.BooleanField(default=False)
    is_past_deployments = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """Override the save method to auto-generate the slug"""
        if not self.id:
            base_slug = slugify(self.preferred_display_name)
            slug = base_slug
            counter = 1
            while UserProfile.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        print(f"Saving UserProfile {self.id} with slug {self.slug}")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Get the absolute URL for the user's public profile"""
        return reverse('public_profile', args=[str(self.id)])


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Existing users: just save the profile
        instance.userprofile.save()


class FollowList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='following')
    followed_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                      related_name='followers')

    def __str__(self):
        """String representation of the FollowUser model"""
        return '{} follow {}'.format(
            self.user.username, self.followed_user.preferred_display_name
        )
