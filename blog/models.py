from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# Post filter options
STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Author(models.Model):
    """
    A model to create the Author
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        )
    profile_picture = CloudinaryField(
        "image",
        default="placeholder"
        )

    def __str__(self):
        return self.user.username


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
    slug = models.SlugField()
    thumbnail = CloudinaryField(
        "image",
        default="placeholder"
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
        Author,
        on_delete=models.CASCADE
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
        default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    A model to create the Comments
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
        )
    name = models.CharField(
        max_length=80
        )
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    approved = models.BooleanField(
        default=False
        )

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
