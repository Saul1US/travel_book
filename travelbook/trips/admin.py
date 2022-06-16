from django.contrib import admin
from .models import Trip, Place, PlaceImage


class PlaceImageAdmin(admin.StackedInline):
    model = PlaceImage
 
# @admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    # list_display = ('name', 'date', 'trip', )
    inlines = [PlaceImageAdmin]
 
    class Meta:
       model = Place
 
# @admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trip)
admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage, PlaceImageAdmin)
