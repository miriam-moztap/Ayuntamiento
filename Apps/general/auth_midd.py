from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

class Authentication(object):

    user = None

    def get_user(self, request):
        jwt_auth = JWTAuthentication()
        try:
            user, _ = jwt_auth.authenticate(request)
            if user:
                self.user = user
                return user
        except AuthenticationFailed:
            pass
        return None

    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        if user is not None:
            return super().dispatch(request, *args, **kwargs)
        response = Response({'message': 'Token invalido'},
                            status=status.HTTP_401_UNAUTHORIZED)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response
