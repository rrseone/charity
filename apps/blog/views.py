from django.views.generic import ListView, DetailView
from taggit.models import Tag

from .models import Post, Category
from django.shortcuts import get_object_or_404


class PostListView(ListView):
    model = Post
    template_name = 'pages/blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.active().filter(status='published').order_by('-published_date')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_title'] = 'All Post'
        context['recent_posts'] = Post.objects.filter(status='published').order_by('-published_date')[:4]
        context['categories'] = Category.objects.active()
        context['tags'] = Tag.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False, is_active=True, status='published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_title'] = self.object.title
        context['recent_posts'] = Post.objects.active().filter(status='published').order_by('-published_date')[:4]
        context['categories'] = Category.objects.active()
        context['tags'] = Tag.objects.all()
        return context


class CategoryPostListView(ListView):
    model = Post
    template_name = 'pages/blog/post_list_by_category.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return Post.objects.filter(category=self.category, status='published').order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_title'] = self.category.title
        context['category'] = self.category
        context['recent_posts'] = Post.objects.filter(status='published').order_by('-published_date')[:4]
        context['categories'] = Category.objects.active()
        context['tags'] = Tag.objects.all()
        return context


class TagPostListView(ListView):
    model = Post
    template_name = 'pages/blog/post_list_by_tag.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
        return Post.objects.filter(tags=self.tag, status='published').order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_title'] = self.tag.name
        context['tag'] = self.tag
        context['recent_posts'] = Post.objects.filter(status='published').order_by('-published_date')[:4]
        context['categories'] = Category.objects.active()
        context['tags'] = Tag.objects.all()
        return context
