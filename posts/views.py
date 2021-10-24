from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorNorReadOnly


class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorNorReadOnly,)
    queryset = Post.objects.all()
    # context_data = {"first_author": get_user_model().objects.filter(id=1)}
    serializer_class = PostSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        # Update context data to add new data
        context.update({"first_author": get_user_model().objects.filter(id=2)})
        return context


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
