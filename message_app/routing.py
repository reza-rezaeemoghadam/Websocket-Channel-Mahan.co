from django.urls import path

from message_app.consumers import MessageConsumer

ws_urlpatterns = [ 
    path('ws/message/<int:company_id>/', MessageConsumer.as_asgi()),
]