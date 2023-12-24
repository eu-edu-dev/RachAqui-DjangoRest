from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views
from django.urls import path, include

from accounts.views import CreateUserView, MeAPIView

urlpatterns = [
    path('me/', MeAPIView.as_view(), name='my_user'),
    path('create-user/', CreateUserView.as_view(), name='create-user-api'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
