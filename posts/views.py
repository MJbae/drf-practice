from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorNorReadOnly


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorNorReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
