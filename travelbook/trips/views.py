from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Trip, Place, PlaceImage


def home(request):
    return render(request, 'trips/home.html')

def trip(request, id):
    trip = get_object_or_404(Trip, id=id)
    return render(request, 'trips/trip.html', {'trip':trip})

# def trip_list_view(request):
#     places = Place.objects.all()
#     return render(request, 'trips/trip_list.html', {'places':places})
 
def place_details_view(request, id):
    place = get_object_or_404(Place, id=id)
    photos = PlaceImage.objects.filter(place=place)
    return render(request, 'trips/place_details.html', {'place':place, 'photos':photos, })


class TripListView(generic.ListView):
    model = Trip
    context_object_name = 'trips'
    template_name = 'trips/trip_list.html'


class PlaceListView(generic.ListView):
    model = Place
    context_object_name = 'places'
    template_name = 'trips/place_list.html'


class PlaceDetailView(generic.DetailView):
    model = Place
    template_name = 'trips/place_details.html'
