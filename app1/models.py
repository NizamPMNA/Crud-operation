from django.db import models

# Create your models here.
class LanguageInfo(models.Model):
    language = models.CharField(max_length=100,null=True)
    designed_by = models.CharField(max_length=100,null=True)
    developer = models.CharField(max_length=500,null=True)
    os = models.CharField(max_length=100,default='-')
    year = models.IntegerField(null=True)
    description = models.TextField()