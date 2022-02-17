
from django.contrib import admin
from django.urls import path,include


from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/',include('users_list.urls')),
    path('api-auth/',include('rest_framework.urls')),

]
