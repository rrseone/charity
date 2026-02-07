import os

from django.templatetags.static import static
from taggit.models import Tag

from apps.blog.models import Category, Post
from apps.charity.models import OptionText, OptionFile, SiteSocialLink


def global_data(request):
    socials = SiteSocialLink.objects.active().order_by('priority')
    categories = Category.objects.active().order_by('-title')
    tags = Tag.objects.all()
    recent_posts = Post.objects.filter(status='published').order_by('-published_date')[:4]
    return {
        'categories': categories,
        'tags': tags,
        'recent_posts': recent_posts,
        'socials': socials
    }


def site_options(request):
    context = {}

    # --- TEXT OPTIONS ---
    for opt in OptionText.objects.all():
        context[opt.key] = opt.value

    # --- FILES OPTIONS (static fallback) ---
    for opt in OptionFile.objects.all():
        if opt.file:
            file_path = opt.file.path
        else:
            file_path = None

        if file_path and os.path.exists(file_path):
            context[f"{opt.key}_url"] = opt.file.url
        else:
            context[f"{opt.key}_url"] = static(opt.file.name if opt.file else "")

        context[f"{opt.key}_caption"] = opt.caption or ""

    return context