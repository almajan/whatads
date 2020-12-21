from django.db import models

# Create your models here.

class SendMsg(models.Model):
        text = models.CharField(max_length=255)

class SendImg(models.Model):
        text = models.CharField(max_length=255)

class SendVdo(models.Model):
        text = models.CharField(max_length=255)

class SendVce(models.Model):
        text = models.CharField(max_length=255)
