"""my_django URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import category

from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path, include
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView

from publication_app.views import *

# def empty_view(request):
#     return HttpResponse("Empty View")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publication_app.urls')),
    path('', include('media_app.urls')),
    path('', include('tags_app.urls')),
    path('', include('comments_app.urls')),
    path('', include('likes_app.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # path('', main_page, name='main_page'),
    # path('list_categories/', category, name='category'),
    # path('', empty_view, name='empty_view'),
    # path('picture/', )

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

# обрабатываем исключение 404 и в view выводим другое сообщение
handler404 = pageNotFound
