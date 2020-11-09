from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from photos_storage.api.serializers import (
    UserSerializer,
    GroupSerializer,
    AuthSerializer,
    PostAuthSerializer,
    ImagesSerializer
)
from photos_storage.api.objects import ApiAuth, ApiImages


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthViewSet(viewsets.ViewSet):
    serializer_class = PostAuthSerializer

    @staticmethod
    def create(request):
        result = AuthSerializer({'token': ApiAuth.get_token()}).data
        return Response(result)


class ImagesViewSet(viewsets.ViewSet):
    serializer_class = ImagesSerializer

    def get_queryset(self, *args, **kwargs):
        # ipdb.set_trace(context=5)
        profile_id = self.kwargs.get("profile_id")
        if not profile_id:
            return Response({"status": "fail"}, status=403)

    @staticmethod
    def list(request):
        page = request.GET.get('page')
        api_images = ApiImages()
        serializer = ImagesSerializer(api_images.get_images(page))
        return Response(serializer.data)
