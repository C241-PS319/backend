from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=255)
    cause = models.TextField()
    healing = models.TextField()
    prevention = models.TextField()
    cost = models.TextField()
    
    def __str__(self):
        return self.name