from django.test import TestCase

from django.contrib.gis.geos import Point

from places.models import Place


class ModelTests(TestCase):

	def testCreatePlace(self):
		"""
		Test whether the Place model can save an object.
		"""
		lagos = Place.objects.create(
			name = 'Lagos',
			slug = 'lagos',
			description='A big city in Nigeria.', 
			point = Point(3.416061, 6.448706)
		)
		lagos.save()
		
		
	def testGoogleMapsProjection(self):
		"""
		Test whether the Google Maps projection (SRID 900913) is available.
		"""
		point = Point(3.416061, 6.448706)
		point.transform(900913)
