from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from config.response import SuccessResponse, FailedResponse
from app.recommendation.models import Disease
from app.recommendation.serializers import DiseaseSerializer
from app.user_history.models import UserHistory
from app.user_history.serializers import UserHistorySerializer

class UserHistoryAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # picture = request.data['picture']
        # user = request.user
        # diseases = Disease.objects.filter(id=disease_id)

        # if not diseases.exists():
        user_histories = UserHistory.objects.filter(user=request.user)
        serializer = UserHistorySerializer(user_histories, many=True)

        # return FailedResponse('Penyakit tidak ada dalam daftar', [])
        # else:
        #     disease = diseases.first()
        #     serializer = DiseaseSerializer(disease)
        return SuccessResponse('Berhasil mendapatkan rekomendasi', serializer.data)