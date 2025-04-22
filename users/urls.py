from django.urls import path

from .views import TokenView


urlpatterns = [
    path('api/token/', TokenView.as_view(), name='token_obtain_pair'),
]
