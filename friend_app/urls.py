from django.urls import include, path

from friend_app.api.views.router import api_router

urlpatterns = [
    path('api/', include(api_router.urls)),
]
