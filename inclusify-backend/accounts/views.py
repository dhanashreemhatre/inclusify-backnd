from rest_framework.response import Response
from django.conf import settings
import os 
import sys
sys.path.append(os.getcwd())
from .serializer import AccountSerializers
from .models import Account
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
User=settings.AUTH_USER_MODEL
import datetime,jwt
from django.contrib.auth import login as django_login 
# Create your views here.


class RegisterView(APIView):
    def post(self,request):
        serializer=AccountSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'user registered successfully.'})

   

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            raise AuthenticationFailed("User Not Found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        # Use Django's login method to log in the user
        django_login(request, user)

        # Generate JWT token (as you did before)
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        return response
