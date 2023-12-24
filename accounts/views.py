from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.models import UserCostumer, UserRestaurant
from accounts.serializers import UserSerializer

User = get_user_model()


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self, request, *arg, **kwargs):
        data = request.data
        is_costumer: bool = data.get('is_costumer')
        data.pop('is_costumer', None)
        user_model = UserCostumer if is_costumer else UserRestaurant
        if not User.objects.filter(email=data.get('email')).exists():
            user = user_model.objects.create_user(**data)
            serialized_user = self.get_serializer(user)
            return Response(serialized_user.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class MeAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        instance = User.objects.get(pk=request.user.pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
