from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Post
from post.serializers import PostDetailSerializer, PostListSerializer, PostLikeUnLikeSerializer


class PostCreateView(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()


class PostLikeUnLikeView(generics.UpdateAPIView):
    serializer_class = PostLikeUnLikeSerializer
    queryset = Post.objects.all()

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        if kwargs.get('type') == 'like':
            obj.likes += 1
        else:
            if obj.likes != 0:
                obj.likes -= 1
            else:
                obj.likes = 0

        obj.save()
        return self.partial_update(request, *args, **kwargs)
