from django.db import models
from app.authentication.models import User
from app.authentication.constants import DEFAULT_USER_PICTURE
from app.recommendation.models import Disease

class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.URLField(default=DEFAULT_USER_PICTURE)
    recommendation = models.ForeignKey(Disease, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name