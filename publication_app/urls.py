from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', main_page),
    path('cats/<int:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]

# handler404 = pageNotFound