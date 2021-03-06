"""digitalplanetbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import RegisterView,EmailView,EmailView2
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
   
    path('register/',RegisterView.as_view(),name='register'),
    # path('verifyemail/',VerifyEmail.as_view(),name='verify'),
    path('test/',EmailView.as_view(),name='email'),
    path('test2/',EmailView2.as_view(),name='email2'),

    path('token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),

    path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),


]
