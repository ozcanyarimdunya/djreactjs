from django.urls import path

from .views import (
    TaskCreateApiView,
    TaskDetailApiView,
    TaskUpdateApiView,
    TaskDeleteApiView,
    TaskListApiView,
)

app_name = 'task'
urlpatterns = [
    path('', TaskListApiView.as_view(), name="list"),
    path('create/', TaskCreateApiView.as_view(), name="create"),
    path('<int:pk>/', TaskDetailApiView.as_view(), name="detail"),
    path('<int:pk>/update/', TaskUpdateApiView.as_view(), name="update"),
    path('<int:pk>/delete/', TaskDeleteApiView.as_view(), name="delete"),
]
