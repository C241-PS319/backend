import requests
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from config.response import SuccessResponse, FailedResponse
from app.user_report.models import UserReportCategory
from app.user_report.serializers import (
    UserReportCategorySerializer,
    CreateUserReportSerializer,
)

class UserReportCategoryAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categories = UserReportCategory.objects.all()
        serializer = UserReportCategorySerializer(categories, many=True)
        return SuccessResponse('success to fetch user report categories data', serializer.data)

class CreateUserReportAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = {
            "user": request.user.id,
            "category":request.data['category'],
            "content":request.data['content']
        }
        serializer = CreateUserReportSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse('success to create user report', serializer.data)
        else:
            return FailedResponse('validation error', serializer.errors)