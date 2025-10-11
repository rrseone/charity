from django.urls import path
from .views import PostListView, PostDetailView, CategoryPostListView, TagPostListView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:category_slug>/', CategoryPostListView.as_view(), name='post_list_by_category'),
    path('tag/<slug:tag_slug>/', TagPostListView.as_view(), name='post_list_by_tag'),
]