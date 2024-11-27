from django.urls import path

from message_app.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]