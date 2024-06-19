from django.urls import path
from app.user_history.views import (
    UserHistoryAPIView,
)

urlpatterns = [
   path('', UserHistoryAPIView.as_view(), name='path_user_history_api'),
]