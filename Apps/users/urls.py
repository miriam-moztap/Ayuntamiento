from django.urls import path
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import CreateNewUserView, LoginAndRegisterUserView, LoginUserView



# urlpatterns = [
#     path('', CreateUserView.as_view(), name='user'),
#     #path('all-users/', ListUpdateDeleteUser.as_view()),
#     #path('role/<int:role_id>/', views.UserRoleListView.as_view(), name='role-list'),
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('tokenRefreshView', TokenRefreshView.as_view(), name='token_refresh'),
#     path('token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
#     path('create_superuser/', CreateSuperUserView.as_view, name='create_superuser'),
# ]


urlpatterns = [
    path('register/', CreateNewUserView.as_view()),
    path('login/', LoginAndRegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokenRefreshView', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
   
]