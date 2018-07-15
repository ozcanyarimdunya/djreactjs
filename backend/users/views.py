from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserDetailsSerializer


class ObtainAuthTokenAPIView(APIView):
    serializer_class = AuthTokenSerializer
    http_method_names = ('post',)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_details = UserDetailsSerializer(instance=user).data
        user_details['token'] = str(token)
        return Response(user_details)
