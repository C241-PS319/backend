from smtplib import SMTPException
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.core.validators import EmailValidator
from config.response import SuccessResponse, FailedResponse
from app.authentication.models import User
from app.authentication.serializers import (
    RegisterUserSerializer,
    LoginSerializer,
    UserSerializer,
    EditUserSerializer,
)
from config.firebase import firebase_verify_id_token

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        password_confirm = request.data['password_confirm']

        if (password != password_confirm):
            return FailedResponse('password must be same as confirm password', None)

        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            registered_user = User.objects.get(email=email)
            user_serializer = UserSerializer(registered_user)
            refresh = RefreshToken.for_user(registered_user)
            response_data = {
                'user': user_serializer.data,
                'token': str(refresh.access_token),
            }
            return SuccessResponse('user registered successfully', response_data)
        else:
            errors = serializer.errors
            return FailedResponse('validation error', errors)

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']

        try:
            user = User.objects.get(email=email)
        except:
            return FailedResponse('user not found!', None)

        if not check_password(password, user.password):
            return FailedResponse('incorrect password!', None)

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        response_data = {
            'token': str(refresh.access_token)
        }
        return SuccessResponse('login successful', response_data)

class GoogleAuthAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        firebase_id_token = request.data['firebase_id_token']
        verified_user = firebase_verify_id_token(firebase_id_token)

        if verified_user is None:
            return FailedResponse('firebase id token expired', None)

        name = verified_user['name']
        email = verified_user['email']
        picture = verified_user['picture']
        firebase_uid = verified_user['uid']

        user = User.objects.filter(email=email).first()
        data = {
            "name": name,
            "email": email,
            "picture": picture,
            "phone": "0",
            "password": firebase_uid
        }

        if user is None: # Register
            serializer = RegisterUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                registered_user = User.objects.filter(email=email).first()
                refresh = RefreshToken.for_user(registered_user)
                response_data = {
                    'token': str(refresh.access_token),
                    'info': 'new registered user'
                }
                return SuccessResponse('google auth login successful', response_data)
            else:
                errors = serializer.errors
                return FailedResponse('validation error', errors)

        else: # Login
            refresh = RefreshToken.for_user(user)
            response_data = {
                'token': str(refresh.access_token),
                'info': 'new registered user'
            }
            return SuccessResponse('google auth login successful', response_data)

class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return SuccessResponse('user details retrieved successfully', serializer.data)

class EditUserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = EditUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse('user details updated successfully', serializer.data)
        else:
            return FailedResponse('validation error', serializer.errors)