from django.db import models

# Create your models here.
class Boy(models.Model):
    name = models.CharField(max_length=32)

class Girl(models.Model):
    name = models.CharField(max_length=32)


class Love(models.Model):
    b = models.ForeignKey('Boy')
    g = models.ForeignKey('Girl')
    t = models.DateTimeField('时间',auto_now=True)