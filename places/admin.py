from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from places.models import Place

class PlaceAdmin(OSMGeoAdmin):
	search_fields = ['name']
	prepopulated_fields = {"slug": ("name",)}
	# Admin map settings
	layerswitcher = False
	scrollable = False
	map_width = 700
	map_height = 325

admin.site.register(Place, PlaceAdmin)
