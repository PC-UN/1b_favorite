from django.db import models

# Create your models here.
class Favourite(models.Model):
    user_id = models.IntegerField()
    place_id = models.IntegerField()
    comment = models.TextField()
