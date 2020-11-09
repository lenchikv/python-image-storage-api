from django.contrib.auth.models import User, Group

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PostAuthSerializer(serializers.Serializer):
    pass


class AuthSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=256)

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class ImageSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    cropped_picture = serializers.CharField(max_length=512)


class ImagesSerializer(serializers.Serializer):
    pictures = serializers.ListSerializer(child=ImageSerializer())
    page = serializers.IntegerField()
    pageCount = serializers.IntegerField()


# TODO implement nested router
class ImageDetailsSerializer (ImageSerializer):
    author = serializers.CharField(max_length=128)
    camera = serializers.CharField(max_length=255)
    tags = serializers.CharField(max_length=512)
    full_picture = serializers.CharField(max_length=512)

    def create(self, validated_data):
        print('image_id', self.kwargs['image_id'])
