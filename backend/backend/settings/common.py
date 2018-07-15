from .base import *

# LOGIN_URL = "/login/"

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'tasks.apps.TasksConfig',
    'categories.apps.CategoriesConfig',
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "backend/assets/media")

REST_FRAMEWORK = {
    # 'DEFAULT_RENDERER_CLASSES': (
    #         'rest_framework.renderers.JSONRenderer',
    # ),
    # 'DEFAULT_PARSER_CLASSES': (
    #         'rest_framework.parsers.JSONParser',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    # "DEFAULT_PERMISSION_CLASSES": (
    # 'rest_framework.permissions.IsAuthenticated',
    # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    # ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}
