from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include('categories.urls')),
    path('task/', include('tasks.urls')),
    path('user/', include('users.urls')),
]
