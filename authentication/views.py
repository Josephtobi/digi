from django.shortcuts import render
from rest_framework import generics,status,views
from .serializers import RegisterSerializers,EmailVerifySerializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .utils import Util 
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.

class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializers

    def post(self, request):
        user= request.data
        serializer=self.serializer_class(data=user)    
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data

        user=CustomUser.objects.get(email=user_data['email'])

        token=RefreshToken.for_user(user).access_token
        current_site=get_current_site(request)
        relativeLink=reverse('verify')
        absurl='http://'+str(current_site)+relativeLink+'?token='+str(token)
        body='Hi \n'+'Pls verify your email with the link below \n'+absurl
        data={
            'subject':'Verify your Email',
            'body':body,
            'to':user.email

        }

        Util.send_email(data)


        return Response(user_data,status.HTTP_201_CREATED)

class VerifyEmail(views.APIView):
    serializer_class=EmailVerifySerializers

    token_param=openapi.Parameter('token',in_=openapi.IN_QUERY, Description='token sent along side email', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param])
    def get(self, request):
        token=request.GET.get('token')

        try:
            payload = jwt.decode(token,settings.SECRET_KEY)

            user= CustomUser.objects.get(id=payload['user_id'])
            user.email_verification=True
            user.save()
            return Response({'message':'email successfully verified'},status.HTTP_200_OK)

        except jwt.ExpiredSignatureError:
            return Response({'message':'token expired'},status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'message':'invalid token request new one'},status.HTTP_400_BAD_REQUEST)
            
            




# class ProjectView(generics.GenericAPIView):
#     serializer_class=''

#     def post(self, request):
#         project=request.data
        