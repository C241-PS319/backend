from django.contrib import admin
from app.user_report.models import ( 
    UserReportCategory,
    UserReport,
)

@admin.register(UserReportCategory)
class UserReportCategory(admin.ModelAdmin):
    fields = []
    list_display = ['id', 'name']

@admin.register(UserReport)
class UserReport(admin.ModelAdmin):
    fields = []
    list_display = ['id', 'user', 'category', 'content', 'created_at']