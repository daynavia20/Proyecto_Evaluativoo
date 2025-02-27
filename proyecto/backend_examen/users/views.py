from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import default_token_generator
from users.serializers import InputUserSerializer, InputEditUserSerializer, OutputUserSerializer,OutPutUserDetailSerializer, LoginInputSerializer, LoginOutputSerializer
from users.models import CustomUser

# Create your views here.
class signUpView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        try:
            serializer = InputUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            if CustomUser.objects.filter(username=serializer.validated_data["username"]).exists():
                return Response({'Error': 'El usuario ya está registrado'}, status=status.HTTP_400_BAD_REQUEST)
            
            if CustomUser.objects.filter(email=serializer.validated_data["email"]).exists():
                return Response({'Error':'El email ya está registrado'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = CustomUser.objects.create(
            username=serializer.validated_data["username"],
            first_name=serializer.validated_data["first_name"],
            last_name=serializer.validated_data["last_name"],
            email=serializer.validated_data["email"],
            phone=serializer.validated_data["phone"],
            create_date=serializer.validated_data["create_date"],
            birth_date=serializer.validated_data["birth_date"],
            )
            
            user.set_password(serializer.validated_data["password"])  
            user.save()
            
            refresh = RefreshToken.for_user(user)
            
            serializer = OutputUserSerializer({
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "phone": user.phone,
                "create_date": user.create_date,
                "birth_date": user.birth_date,
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            })
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as a:
            return Response({"Error": str(a)}, status=status.HTTP_400_BAD_REQUEST)
        
class editUserView(APIView):
    permission_classes = [AllowAny]

    def patch(self, request, pk=None):
        try:
            user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"Error": "El usuario no existe"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InputEditUserSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            for key, value in serializer.validated_data.items():
                setattr(user, key, value)
            user.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
class detailUserView(APIView):
    permission_classes = [AllowAny]  
    
    def get(self, request, pk=None):
        try:
            user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"Error": "el usuario no exite"}, status=status.HTTP_404_NOT_FOUND)
        serializer = OutPutUserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class listUserView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            user = CustomUser.objects.all()
            serializer = OutPutUserDetailSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as a:
            return Response({"Error": str(a)}, status=status.HTTP_400_BAD_REQUEST)
        
class loginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            user = CustomUser.objects.get(username=serializer.validated_data['username'])
        except CustomUser.DoesNotExist:
            return Response({'Error':'Usuario es incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
        
        is_password_correct = user.check_password(serializer.validated_data['password'])
        if is_password_correct is False:
            return Response({'Error': 'Contraseña es incorrecta'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)

        serializer = LoginOutputSerializer({
            "id": user.id,
            "username": user.username,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            
        })
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
