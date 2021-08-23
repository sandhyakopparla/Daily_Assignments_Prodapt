from django.db import models
class Cricket(models.Model):
    cricketer_name=models.CharField(max_length=50)
    matchone_score=models.CharField(max_length=50)
    matchtwo_score=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    team=models.CharField(max_length=50)
    batting_style=models.CharField(max_length=50)
    bowling_style=models.CharField(max_length=50)
    
