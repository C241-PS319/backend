from rest_framework import serializers
from app.user_history.models import UserHistory
from app.recommendation.serializers import DiseaseSerializer

class UserHistorySerializer(serializers.ModelSerializer):
    recommendation = DiseaseSerializer()
    class Meta:
        model = UserHistory
        fields = ['id', 'picture', 'created_at', 'recommendation']