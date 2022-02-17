from django.urls import path
from .views import UserListView, UserUpdateView

urlpatterns = [
    path('users',
         UserListView.as_view(),
         name='user_list_api'
         ),

    path('users/<int:pk>',
        UserUpdateView.as_view(),
        name='user_detail_api'
    ),
]