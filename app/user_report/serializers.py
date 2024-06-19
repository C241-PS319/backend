from rest_framework import serializers
from app.user_report.models import (
    UserReportCategory,
    UserReport,
)

class UserReportCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReportCategory
        fields = '__all__'

class CreateUserReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReport
        fields = ['user', 'category', 'content']