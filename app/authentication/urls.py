from django.urls import path
from app.authentication.views import (
    RegisterAPIView,
    LoginAPIView,
    GoogleAuthAPIView,
    UserAPIView,
    EditUserAPIView,
)

urlpatterns = [
   path('register/', RegisterAPIView.as_view(), name='path_register_api'),
   path('login/', LoginAPIView.as_view(), name='path_login_api'),
   path('google-auth/', GoogleAuthAPIView.as_view(), name='path_google_auth_api'),
   path('user/', UserAPIView.as_view(), name="path_user_api"),
   path('user/edit/', EditUserAPIView.as_view(), name="path_user_edit_api"),
]