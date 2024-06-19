from rest_framework import serializers
from app.recommendation.models import Disease

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__' 