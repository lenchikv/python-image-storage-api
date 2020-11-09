from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('photos_storage.api.urls')),
    path('admin/', admin.site.urls),
]
