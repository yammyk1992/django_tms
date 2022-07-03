from django.contrib.auth.decorators import login_required
from django.urls import path, include

from .api.views.router import api_router
from .views import TagsView

urlpatterns = [
    path('api/', include(api_router.urls)),
    path('tag/<str:tag', login_required(TagsView.as_view()), name='tags'),
]