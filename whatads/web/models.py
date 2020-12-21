from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __unicode__(self):
        return (self.user)

class SendMsg(models.Model):
        text = models.CharField(max_length=255)
        def __unicode__(self):
            return self.text

class SendImg(models.Model):
        text = models.CharField(max_length=255)
        def __unicode__(self):
            return self.text

class SendVdo(models.Model):
        text = models.CharField(max_length=255)
        def __unicode__(self):
            return self.text

class SendVce(models.Model):
        text = models.CharField(max_length=255)
        def __unicode__(self):
            return self.text


class CheckDlvy(models.Model):
        text = models.CharField(max_length=255)
        def __unicode__(self):
            return self.text

class CheckSeen(models.Model):
        text = models.CharField(max_length=255)
        def __unicode__(self):
            return self.text
