from django.contrib import admin
from app.recommendation.models import ( 
    Disease,
)

@admin.register(Disease)
class Disease(admin.ModelAdmin):
    fields = []
    list_display = ['id', 'name', 'cause', 'healing', 'prevention', 'cost']