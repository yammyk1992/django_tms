from django.urls import path, include

from .api.views.router import api_router
from media_app.api.views.media import MediaViewSet

urlpatterns = [
    path('api/', include(api_router.urls)),
]
