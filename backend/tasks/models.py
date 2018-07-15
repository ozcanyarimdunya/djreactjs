from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from categories.models import Category

User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='members')
    is_done = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
