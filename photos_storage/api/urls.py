from django.urls import include, path
from rest_framework import routers
from photos_storage.api import views

router = routers.DefaultRouter()
router.register(r'auth', views.AuthViewSet, basename='auth')
router.register(r'images', views.ImagesViewSet, basename='images')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]

