from django.db import models

# Create your models here.

class WerckerModels(models.Model):
    TokenName = models.CharField(max_length=20)
    Token = models.CharField(max_length=200)
    


