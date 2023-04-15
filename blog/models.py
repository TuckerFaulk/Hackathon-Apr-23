from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from profiles.models import UserProfile
from django.utils.text import slugify

# Create your models here.

# Post filter options
STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Category(models.Model):
    """
    A model to create the Post categories
    """
    title = models.CharField(
        max_length=50
        )
    subtitle = models.CharField(
        max_length=50
        )

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    A model to create the Post content
    """
    title = models.CharField(
        max_length=200
        )
    slug = models.SlugField()
    excerpt = models.TextField()
    updated_on = models.DateTimeField(
        auto_now=True
        )
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True
        )
    content = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    featured_image = CloudinaryField(
        'image',
        default='placeholder'
        )
    categories = models.ManyToManyField(
        Category
        )
    status = models.IntegerField(
        choices=STATUS,
        default=1
        )
    likes = models.ManyToManyField(
        User, related_name='blogpost_like',
        blank=True
        )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def author_name(self):
        return self.UserProfile.preferred_display_name

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    A model to create the Comments
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
        )
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True
        )
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    approved = models.BooleanField(
        default=True
        )

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
