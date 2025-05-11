from django.contrib.auth import authenticate
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from django.http.response import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import ProfileSerializer
from django.contrib.auth.models import User 
from todo.serializers import LoginSerializer

class TokenView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': 'Invalid credentials'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProfileView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = User.objects.all()

@cache_page(30)
def test_redis(request):
    # cache.set('pass', '12345', timeout=5)
    # value = cache.get('pass')
    import time
    start = time.time()
    time.sleep(6)
    duration = time.time() - start
    return HttpResponse(f"مدت زمان اجرا: {duration} ثانیه")