from django.urls import path

from .views import TokenView, ProfileView, test_redis


urlpatterns = [
    path('api/token/', TokenView.as_view(), name='token_obtain_pair'),
    path('api/profile/', ProfileView.as_view()),
    path('api/redis/', test_redis),
]
