from django.urls import path
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import CreateNewUserView, LoginAndRegisterUserView

urlpatterns = [
    path('register/', CreateNewUserView.as_view()),
    path('login/', LoginAndRegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokenRefreshView', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
]