from django.urls import path

from post.views import PostCreateView, PostListView, PostLikeUnLikeView, PostDetailView

app_name = 'post'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/reaction/<str:type>/', PostLikeUnLikeView.as_view(), name='post-interactive'),
    path('<int:pk>/detail/', PostDetailView.as_view(), name='post-detail'),
]
