from django.template.defaulttags import url

from friend_app import views

urlpatterns = [
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')
]
