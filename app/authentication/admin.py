from django.contrib import admin
from app.authentication.models import ( 
    User,
)

@admin.register(User)
class User(admin.ModelAdmin):
    fields = []
    list_display = ['id', 'name', 'email', 'phone']