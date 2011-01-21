from django.db import models

# Create your models here.

class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True, upload_to="logos")

    def __unicode__(self):
        return self.name
