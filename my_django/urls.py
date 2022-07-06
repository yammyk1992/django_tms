from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path, include
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView

from publication_app.views import pageNotFound


def trigger_error(request):
    division_by_zero = 1 / 0
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publication_app.urls')),
    path('', include('media_app.urls')),
    path('', include('tags_app.urls')),
    path('', include('comments_app.urls')),
    path('', include('likes_app.urls')),
    path('', include('profile_app.urls')),
    path('', include('friend_app.urls')),
    path('', include('subscription_app.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('sentry-debug/', trigger_error),

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
