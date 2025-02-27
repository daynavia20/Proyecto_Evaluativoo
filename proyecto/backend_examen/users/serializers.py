from rest_framework import serializers
from users.models import CustomUser

class InputUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name= serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(min_length=8)
    email = serializers.EmailField()
    phone = serializers.CharField()
    createDate = serializers.DateField(source="create_date")
    birthDate = serializers.DateField(source="birth_date")
    
class OutputUserSerializer(InputUserSerializer):
    password = None
    accessToken = serializers.CharField(source="access_token")
    refreshToken = serializers.CharField(source="refresh_token")

class InputEditUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name= serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    birthDate = serializers.DateField(source="birth_date")
        

class OutPutUserDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    first_name= serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    create_date = serializers.DateField()
    birth_date = serializers.DateField()

class LoginInputSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)
    
    
class LoginOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    accessToken = serializers.CharField(source="access_token")
    refreshToken = serializers.CharField(source="refresh_token")
