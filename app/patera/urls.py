from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # View urls
    path("admin/", admin.site.urls),
    path("prometheus/", include("django_prometheus.urls")),

    # API urls
    path("v1/auth/", include('app.authentication.urls')),
    path("v1/recommendation/", include('app.recommendation.urls')),
    path("v1/user-history/", include('app.user_history.urls')),
    # path("v1/user-report", include('app.user_report.urls')),
]