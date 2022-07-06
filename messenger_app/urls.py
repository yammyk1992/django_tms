from django.urls import include, path

from messenger_app.api.views.router import api_routers

urlpatterns = [
    path('api/', include(api_routers.urls)),
]
