from django.db import models
from taggit.managers import TaggableManager


class Spot(models.Model):
	name = models.CharField(max_length=100)
	suburb = models.CharField(max_length=100)

	lat = models.DecimalField('Latitude', max_digits=12, decimal_places=9)
	lng = models.DecimalField('Longitude', max_digits=12, decimal_places=9)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	tags = TaggableManager()