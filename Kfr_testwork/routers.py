from rest_framework.routers import DefaultRouter
from django.urls import path,include
from users_list.views import AdminViewSet

router = DefaultRouter()
router.register(r'private/users',AdminViewSet, basename='private_users')
urlpatterns = [
    path('',include(router.urls))
]