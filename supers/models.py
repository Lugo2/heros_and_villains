from ssl import ALERT_DESCRIPTION_NO_RENEGOTIATION
from unicodedata import name
from django.db import models

# Create your models here.

class supers(models.Model):
    name = models.CharField(max_length = 250)
    alter_ego = models.CharField(max_length = 250)
    primary_ability = models.CharField(max_length = 400)
    secondary_ability = models.CharField(max_length = 400)
    catch_phrase = models.CharField(max_length = 400)
    super_type = models.ForeignKey()
