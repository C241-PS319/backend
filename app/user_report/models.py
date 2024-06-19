from django.db import models
from app.authentication.models import User

class UserReportCategory(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class UserReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(UserReportCategory, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content