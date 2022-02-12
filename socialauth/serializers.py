from rest_framework import serializers
from .register import register_social_user
import os
from rest_framework.exceptions import AuthenticationFailed


class GoogleSerializer(serializers.Serializer):
    auth_token=serializers.CharField()

    def validate_auth_token(self,auth_token):
        user_data=google.Google.validate(auth_token)

        try:
            user_data['sub']
        except:
            raise serializers.ValidationError('this token is expired')
        
        if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):
            raise AuthenticationFailed('who are you?')


        user_id=user_data['sub']
        email=user_data['email']
        name=user_data['name']

        return register_social_user(
             user_id=user_id, email=email, name=name)
