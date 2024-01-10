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
# Create your views here.


class RegisterView(APIView):
    def post(self,request):
        serializer=AccountSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'user registered successfully.'})

class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        try:
            user=  Account.objects.get(email=email)
        except:
            user=None
        if user is None:
            raise AuthenticationFailed("User Not Found")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")
        
        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }
        token=jwt.encode(payload,'secret',algorithm='HS256')
        resopnse=Response()
        resopnse.set_cookie(key='jwt',value=token,httponly=True)
        resopnse.data={'jwt':token}
        
        return resopnse
   
