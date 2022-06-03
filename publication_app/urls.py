from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from publication_app.api.view.publications import PostsViewSet
from .views import *

urlpatterns = [

                  path('', PostHome.as_view(), name='home'),
                  path('about/', about, name='about'),
                  path('addpage/', AddPage.as_view(), name='add_page'),
                  path('contact/', contact, name='contact'),
                  path('login/', LoginUser.as_view(), name='login'),
                  path('logout/', logout_user, name='logout'),
                  path('register/', RegisterUser.as_view(), name='register'),
                  path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
                  path('category/<slug:category_slug>/', PostCategory.as_view(), name='category'),
                  path('tag/<slug:tag_slug>', tags, name='tags'),
                  path('api/posts', PostsViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}, name='api-posts')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
