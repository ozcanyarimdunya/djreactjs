from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from .models import Category


class CategoryCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]


class CategoryDetailSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='category:detail'
    )

    class Meta:
        model = Category
        fields = [
            'url',
            'id',
            'name',
            'timestamp',
        ]


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'timestamp',
        ]
