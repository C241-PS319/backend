from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from config.response import SuccessResponse, FailedResponse
from app.recommendation.models import Disease
from app.recommendation.serializers import DiseaseSerializer

class RecommendationAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, disease_id):
        picture = request.data['picture']
        user = request.user
        diseases = Disease.objects.filter(id=disease_id)

        if not diseases.exists():
            return FailedResponse('Penyakit tidak ada dalam daftar')
        else:
            disease = diseases.first()
            serializer = DiseaseSerializer(disease)
            return SuccessResponse('Berhasil mendapatkan rekomendasi', serializer.data)