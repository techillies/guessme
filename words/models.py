from django.db import models

# Create your models here.


class Words(models.Model):
    name = models.CharField(max_length=20, unique=True)
    subword1 = models.CharField(max_length=20)
    subword2 = models.CharField(max_length=20)
    subword3 = models.CharField(max_length=20)
    subword4 = models.CharField(max_length=20)
    subword5 = models.CharField(max_length=20)

    def __unicode__(self):
        return "%s:" % (self.name)
