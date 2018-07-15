from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import AllowAny

from .models import Category
from .serializers import (
    CategoryCreateUpdateSerializer,
    CategoryDetailSerializer,
    CategoryListSerializer
)


class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateUpdateSerializer

    def perform_create(self, serializer):
        from django.contrib.auth.models import User
        serializer.save(user=User.objects.first())


class CategoryDetailApiView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CategoryUpdateApiView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateUpdateSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class CategoryDeleteApiView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [AllowAny]
