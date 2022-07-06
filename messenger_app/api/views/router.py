from rest_framework import routers

from messenger_app.api.views.messenger import MessengerView

api_routers = routers.DefaultRouter()
api_routers.register('messages', MessengerView)
