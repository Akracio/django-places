from django.contrib.gis.db import models

class Place(models.Model):
	"""
	A point. Maybe a city. Maybe a pothole.
	"""
	name = models.CharField(max_length=500)
	slug = models.SlugField(unique=True)
	description = models.TextField()
	point = models.PointField(null=True, blank=True)
	objects = models.GeoManager()
	
	class Meta:
		ordering = ('name',)
		
	def __unicode__(self):
		u'%s (%4f, %4f)' % (self.name, self.point.x, self.point.y)