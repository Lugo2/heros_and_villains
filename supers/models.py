from django.db import models
from super_types.models import SuperTypes

# Create your models here.

class Supers(models.Model):
    name = models.CharField(max_length = 250)
    alter_ego = models.CharField(max_length = 250)
    primary_ability = models.CharField(max_length = 400)
    secondary_ability = models.CharField(max_length = 400)
    catch_phrase = models.CharField(max_length = 400)
    super_type = models.ForeignKey(SuperTypes, on_delete = models.CASCADE)
