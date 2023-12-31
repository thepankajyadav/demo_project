from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer
from .renderers import UserRenderer



# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class CreateUserView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        serialized_user = UserSerializer(user).data 
        token = get_tokens_for_user(user)
        return Response({'token':token, 'user': serialized_user, 'msg':'User created'}, status=status.HTTP_201_CREATED)