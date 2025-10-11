from django.db import models
from django_countries.fields import CountryField

from apps.base.middlewares import get_current_user
from apps.base.utils import UploadToPathAndRename, SPONSOR_LEVEL_CHOICES

from django.conf import settings

User = settings.AUTH_USER_MODEL


class BaseModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def active(self):
        return self.get_queryset().filter(is_active=True)


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        User,
        related_name="created_%(class)s",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        editable=False,
    )
    updated_by = models.ForeignKey(
        User,
        related_name="updated_%(class)s",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        editable=False,
    )

    objects = BaseModelManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            if not self.pk:
                self.created_by = user
            self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        super().save(*args, **kwargs)
        return

class City(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    country = CountryField(blank_label='Select Country', null=True)

    def __str__(self):
        return f'{self.name}, {self.country.name}'

class Role(BaseModel):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Member(BaseModel):
    is_featured = models.BooleanField(default=False)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=UploadToPathAndRename('images'), null=True)

    def social_links(self):
        return SocialLink.objects.active().filter(member=self)

    def __str__(self):
        return self.full_name

class Social(BaseModel):
    title = models.CharField(max_length=255)
    fontawesome_class = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class SocialLink(BaseModel):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    social = models.ForeignKey(Social, on_delete=models.CASCADE)
    link = models.URLField(max_length=255)

    def __str__(self):
        return f'{self.member.full_name}, {self.social.title}, {self.link}'


class Sponsor(BaseModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=UploadToPathAndRename('logo'), null=True)
    link = models.URLField(max_length=255)
    level = models.CharField(choices=SPONSOR_LEVEL_CHOICES, max_length=255, default='silver')

    def __str__(self):
        return self.name


class Option(BaseModel):
    key = models.SlugField(max_length=255, unique=True)
    value = models.CharField(max_length=255, null=True)
    priority = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.key

    class Meta:
        ordering = ['priority']




