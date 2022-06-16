from django.shortcuts import render, get_object_or_404
from .models import Trip, Place, PlaceImage


def home(request):
    return render(request, 'trips/home.html')

def trip_list_view(request):
    places = Place.objects.all()
    return render(request, 'trips/trip_list.html', {'places':places})
 
def place_details_view(request, id):
    place = get_object_or_404(Place, id=id)
    photos = PlaceImage.objects.filter(place=place)
    return render(request, 'trips/place_details.html', {
        'place':place,
        'photos':photos, 
    })
