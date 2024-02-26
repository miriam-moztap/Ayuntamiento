from django.urls import path
from .views import CreateListUser, ListUpdateDeleteUser
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('', CreateListUser.as_view(), name='user'),
    path('all-users/', ListUpdateDeleteUser.as_view()),
    #path('role/<int:role_id>/', views.UserRoleListView.as_view(), name='role-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokenRefreshView', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_refresh')
]