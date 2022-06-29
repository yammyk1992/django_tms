from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from profile_app.views import ProfileEdit
from publication_app.api.view.router import api_router
from .views import *

urlpatterns = [

                  path('', PostHome.as_view(), name='home'),
                  path('about/', about, name='about'),
                  # path('addpage/', addpage, name='add_page'),
                  path('addpage/', AddPage.as_view(), name='add_page'),
                  path('login/', LoginUser.as_view(), name='login'),
                  path('logout/', logout_user, name='logout'),
                  path('register/', Register.as_view(), name='register'),
                  path('post/<int:pk>', login_required(ShowPost.as_view()), name='post'),
                  path('category/<slug:category_slug>/', PostCategory.as_view(), name='category'),
                  path('tag/<slug:tag_slug>', tags, name='tags'),
                  path('user/<int:pk>', login_required(ProfileEdit.as_view()), name='profile_account'),
                  path('api/', include(api_router.urls)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
