from django.urls import path

from .views import ObtainAuthTokenAPIView

app_name = 'user'
urlpatterns = [
    path('get-token/', ObtainAuthTokenAPIView.as_view(), name="get-token")
]
