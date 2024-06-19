from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from config.response import SuccessResponse, FailedResponse
from app.user_history.models import UserHistory
from app.user_history.serializers import UserHistorySerializer

class UserHistoryAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_histories = UserHistory.objects.filter(user=request.user)

        if not user_histories.exists():
            return FailedResponse('Pengguna tidak memiliki riwayat', [])

        serializer = UserHistorySerializer(user_histories, many=True)
        return SuccessResponse('Berhasil mendapatkan riwayat pengguna', serializer.data)