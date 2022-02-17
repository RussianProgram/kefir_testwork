from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly

from .serializers import (
    UserCreateSerializer,
    UserListSerializer,
    UserUpdateSerialiser,
    AdminUserListSerializer,
    AdminUserUpdateSerializer
)

from django.contrib.auth.models import User



"""Создаем Вьюсет для более удобной работы с логикой для амина"""
class AdminViewSet(viewsets.ModelViewSet):
    serializer_class = AdminUserListSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        client_serialiser = self.get_serializer(data=request.data)
        client_serialiser.is_valid(raise_exception=True)
        data = client_serialiser.validated_data
        client_serialiser.save(**data)

        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        pk = kwargs['pk']
        current_user = User.objects.get(pk=pk)
        if (request.user != current_user) and (not request.user.is_staff):
            return Response("Can't change another user profile")
        return super().update(request, *args, **kwargs)


    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        if self.action == 'update':
            return AdminUserUpdateSerializer
        return AdminUserListSerializer

"""Список пользователей"""
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdminOrReadOnly]

"""Обновления пользователем его профиля"""
class UserUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerialiser
    permission_classes = [IsOwnerOrReadOnly]
