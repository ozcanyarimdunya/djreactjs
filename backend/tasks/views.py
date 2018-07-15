from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import AllowAny

from .models import Task
from .serializers import (
    TaskCreateUpdateSerializer,
    TaskDetailSerializer,
    TaskListSerializer
)


class TaskCreateApiView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailApiView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


class TaskUpdateApiView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateUpdateSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class TaskDeleteApiView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


class TaskListApiView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [AllowAny]
