from django.urls import include, path

from comments_app.api.views.router import api_router


urlpatterns = [
    path('api/', include(api_router.urls)),
]