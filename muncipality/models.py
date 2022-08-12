from django.db import models

# Create your models here.

class newBindata(models.Model):
    id=models.AutoField(primary_key=True)
    Binid=models.IntegerField(default=0)
    capacity=models.IntegerField(default=0 )
    muncipality=models.CharField(max_length=100)
    distance=models.IntegerField(default=0)
    longitude=models.FloatField(default=0)
    latitude=models.FloatField(default=0)
    place=models.CharField(max_length=100)
    date_joined=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.Binid