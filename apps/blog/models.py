from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import now
from django_editorjs_fields import EditorJsJSONField
from stdimage import StdImageField
from taggit.managers import TaggableManager

from apps.base.models import BaseModel
from apps.base.utils import UploadToPathAndRename
from apps.blog.utils import POST_STATUS_CHOICES

User = get_user_model()


class Category(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def posts_count(self):
        return Post.objects.active().filter(category=self).count()

    def get_absolute_url(self):
        return reverse('blog:post_list_by_category', kwargs={'category_slug': self.slug})


class Post(BaseModel):
    is_featured = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = StdImageField(
        upload_to=UploadToPathAndRename('images'),
        variations={
            'large': (600, 400, True),
            'thumbnail': (300, 200, True),
            'icon': (80, 80, True),
        },
        delete_orphans=True,
        null=True,
    )
    description = models.TextField()
    content = EditorJsJSONField(blank=True, null=True)
    status = models.CharField(choices=POST_STATUS_CHOICES, max_length=10, default='draft')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    tags = TaggableManager(blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='posts')
    published_date = models.DateTimeField(default=timezone.now)

    def next_post(self):
        return Post.objects.filter(
            published_date__gt=self.published_date,
            status='published'
        ).order_by('published_date').first()

    def previous_post(self):
        return Post.objects.filter(
            published_date__lt=self.published_date,
            status='published'
        ).order_by('-published_date').first()

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def comments(self):
        return Comment.objects.active().filter(post=self).order_by('-created_at')

    def comments_count(self):
        return Comment.objects.active().filter(post=self).count()

    def get_date(self):
        delta = now() - self.published_date

        if delta.days < 1:
            # Less than 24 hours
            hours = delta.seconds // 3600
            return f"{hours} hour{'s' if hours != 1 else ''} ago" if hours > 0 else "Just now"
        elif delta.days < 7:
            # Less than 7 days
            return f"{delta.days} day{'s' if delta.days != 1 else ''} ago"
        else:
            return self.created_at.strftime("%b %d, %Y")


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='author_comments')
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.author.full_name or self.author.email

    class Meta:
        ordering = ['-created_at']

    def get_date(self):
        delta = now() - self.created_at

        if delta.days < 1:
            # Less than 24 hours
            hours = delta.seconds // 3600
            return f"{hours} hour{'s' if hours != 1 else ''} ago" if hours > 0 else "Just now"
        elif delta.days < 7:
            # Less than 7 days
            return f"{delta.days} day{'s' if delta.days != 1 else ''} ago"
        else:
            return self.created_at.strftime("%b %d, %Y")
