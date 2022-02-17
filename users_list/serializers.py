from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

"""Сериализатор для создания юзера"""
class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'password2',
            'email',
            'first_name',
            'last_name',
            'is_staff',
        ]

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()

        return user

"""Сериализатор для вывода списка юзеров"""
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]

"""Сериализатор для обновления юзером его профиля"""
class UserUpdateSerialiser(serializers.ModelSerializer):
    is_staff = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
        ]

"""
Сериализатор для админа выводящий полную информацию о юзерах
"""
class AdminUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
        ]


"""
Сериализатор для админа чтобы обновлять профили юзеров
"""
class AdminUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
        ]