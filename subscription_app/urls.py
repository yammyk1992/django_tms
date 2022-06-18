from django.urls import path

from subscription_app import views

app_name = 'membership'
urlpatterns = [
       path('memberships/', views.MembershipView.as_view(), name='select'),
]