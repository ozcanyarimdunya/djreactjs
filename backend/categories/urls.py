from django.urls import path

from .views import (
    CategoryCreateApiView,
    CategoryDetailApiView,
    CategoryUpdateApiView,
    CategoryDeleteApiView,
    CategoryListApiView,
)

app_name = 'category'
urlpatterns = [
    path('', CategoryListApiView.as_view(), name="list"),
    path('create/', CategoryCreateApiView.as_view(), name="create"),
    path('<int:pk>/', CategoryDetailApiView.as_view(), name="detail"),
    path('<int:pk>/update/', CategoryUpdateApiView.as_view(), name="update"),
    path('<int:pk>/delete/', CategoryDeleteApiView.as_view(), name="delete"),
]
