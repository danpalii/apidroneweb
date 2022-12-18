from django.db import models

class FunctionTurnPointModel(models.Model):
    turn_point = models.IntegerField(blank=True, null=True)

class StatusModel(models.Model):
    status_point = models.IntegerField(blank=True, null=True)

class ImageModel(models.Model):
    image = models.ImageField(upload_to='%Y_%m_%d/', null=True, blank=True, max_length=255)