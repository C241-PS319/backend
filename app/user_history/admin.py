from django.contrib import admin
from app.user_history.models import ( 
    UserHistory,
)

@admin.register(UserHistory)
class UserHistory(admin.ModelAdmin):
    fields = []
    list_display = ['id', 'user', 'picture', 'recommendation', 'created_at']