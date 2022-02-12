from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView
from .serializers import GoogleSerializer


# Create your views here.


class GoogleAPIView(GenericAPIView):
    serializer_class=GoogleSerializer

    def post(self, request):
        serializer=self.serializer_class
        serializer.is_valid(raise_exception=True)

        data= ((serializer.data)['auth_token'])
        return Response(data, status=HTTP_200_OK)
