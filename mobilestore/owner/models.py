from django.db import models

# Create your models here.
class Mobile(models.Model):
    mobile_name=models.CharField(max_length=120,unique=True)
    mobile_model=models.CharField(max_length=100,unique=True)
    company=models.CharField(max_length=100)
    price=models.PositiveIntegerField(default=100)
    def __str__(self):
        return self.mobile_name
