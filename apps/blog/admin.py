from django.contrib import admin

from apps.blog.models import Category, Post, Comment


class CommentTabularInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('author', 'text', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (CommentTabularInline,)
    prepopulated_fields = {"slug": ("title",)}