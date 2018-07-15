from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from categories.serializers import CategoryDetailSerializer
from .models import Task


class TaskCreateUpdateSerializer(ModelSerializer):
    category = CategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'content',
            'category',
            'members',
            'is_done'
        ]

    def category(self, obj):
        return obj.category.pk


class TaskDetailSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='task:detail'
    )
    category = SerializerMethodField()
    members = SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'url',
            'id',
            'name',
            'content',
            'category',
            'members',
            'is_done',
            'timestamp',
        ]

    def get_category(self, obj):
        return dict(id=obj.category.id, name=obj.category.name)

    def get_members(self, obj):
        return obj.members.values('id', 'username').all()


class TaskListSerializer(ModelSerializer):
    category = SerializerMethodField()
    members = SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'content',
            'category',
            'members',
            'is_done',
            'timestamp'
        ]

    def get_category(self, obj):
        return dict(id=obj.category.id, name=obj.category.name)

    def get_members(self, obj):
        return obj.members.values('id', 'username').all()
