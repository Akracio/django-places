from django.test import TestCase

from django.contrib.gis.geos import Point

from places.models import Place


class ModelTests(TestCase):

    def createPlace(self):
        """
        Test whether the Place model can save an object.
        """
        lagos = Change.objects.create(
            name = 'Lagos',
            slug = 'lagos',
            description='A big city in Nigeria.', 
            point = Point(3.416061, 6.448706)
        )
        self.failIfEqual(lagos.pub_date, None)
        lagos.save()

# Could use a test yet to make sure the google maps projection is installed