from rest_framework import exceptions
from rest_framework.authentication import (get_authorization_header,
                                           BaseAuthentication )
import jwt
from django.conf import settings
from .models import myUser

class JWTAuthentication(BaseAuthentication):



    def authenticate(self, request):

        auth_header =get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')

        auth_token = auth_data.split(" ")



        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed('Token not valid')

        token=auth_token[1]


        try:
            payload = jwt.decode(
                token,settings.SECRET_KEY,algorithms='HS256')

            username=payload['email']

            user=myUser.objects.get(email=username)

            return (user,token)



        except jwt.ExpiredSignatureError as ex:
            raise  exceptions.AuthenticationFailed(
                'Token is expired, login again'
            )
       # except myUser.DoesNotExist as no_user:
        #    raise exceptions.AuthenticationFailed(
         #       'No such  user'
          #  )

        except jwt.DecodeError as ex:
            raise  exceptions.AuthenticationFailed(
                'Token is incalid'
            )




        return super().authenticate(request)
