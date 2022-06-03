from django.urls import path

from media_app.api.views.media import MediaViewSet

urlpatterns = [
    path('api/media/', MediaViewSet.as_view({'get': 'retrieve', 'post': 'create'}, name='api-media')),
]
