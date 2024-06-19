from django.urls import path
from app.user_report.views import (
    UserReportCategoryAPIView,
    CreateUserReportAPIView,
)

urlpatterns = [
    path('categories/', UserReportCategoryAPIView.as_view(), name='path_user_report_category_api_view'),
    path('create/', CreateUserReportAPIView.as_view(), name='path_create_user_report_api_view'),
]