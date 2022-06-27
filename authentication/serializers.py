from rest_framework import serializers
from .models import CustomUser



class RegisterSerializers(serializers.ModelSerializer):
    password=serializers.CharField(
        max_length=68, min_length=5, write_only=True
    )

    class Meta:
        model = CustomUser
        fields=['email','password','username','first_name','last_name','link','location','bio','skills']

    def validate(self, attrs):
        email=attrs.get('email', '')
        username=attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError('The username must be alphanumeric')
        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
        #this function is called when you say saved on the view 

class EmailVerifySerializers(serializers.ModelSerializer):
    token=serializers.CharField(max_length=500)

    class Meta:
        model=CustomUser
        fields=['token']

class EmailSerializers(serializers.Serializer):
    email=serializers.CharField(max_length=500)
    
class EmailSerializers2(serializers.Serializer):
    token=serializers.CharField(max_length=500)
