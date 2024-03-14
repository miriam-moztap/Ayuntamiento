from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from django.utils import timezone
from django.conf import settings

from datetime import timedelta

class ExpiringJWTAuthentication(JWTAuthentication):

    def expires_in(self, token):
        role_id = token.payload['role_id']
        if role_id == 2:
            time_elapsed = timezone.now() - token.created_at
            left_time = timedelta(seconds=int(settings.ADMIN_TOKEN_EXPIRED_AFTER_SECONDS)) - time_elapsed
            return left_time
        time_elapsed = timezone.now() - token.created_at
        left_time = timedelta(seconds=int(settings.TOKEN_EXPIRED_AFTER_SECONDS)) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire(self, token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            payload = token.payload
            user = payload['user_id']
            access_token = AccessToken.for_user(user)
            token = access_token
        return token

    def authenticate(self, request):
        user = None
        try:
            raw_token = self.get_raw_token(request)
            validated_token = self.get_validated_token(raw_token)
            token = self.token_expire(validated_token)
            user = token.payload['user_id']
        except AuthenticationFailed:
            pass

        return user, token
