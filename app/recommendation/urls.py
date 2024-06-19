from django.urls import path
from app.recommendation.views import (
    RecommendationAPIView,
)

urlpatterns = [
   path('<int:disease_id>/', RecommendationAPIView.as_view(), name='path_recommendation_api'),
]