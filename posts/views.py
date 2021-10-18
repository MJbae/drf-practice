from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorNorReadOnly


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorNorReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
