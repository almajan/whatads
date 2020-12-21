from django.db import models

# Create your models here.

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
