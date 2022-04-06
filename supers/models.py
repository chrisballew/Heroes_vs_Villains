from django.db import models
from super_types.models import Super_Type


class Power(models.Model):
    name = models.CharField(max_length=255)
# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    # primary_ability = models.CharField(max_length=255)
    # secondary_ability = models.CharField(max_length=255)
    powers = models.ManyToManyField(Power)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(Super_Type, on_delete=models.CASCADE)


