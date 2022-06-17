from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import generic
from .models import Trip, Place, PlaceImage


def index(request):
    return render(request, 'trips/index.html')

def home(request):
    trips_count = Trip.objects.all().count()
    places_count = Place.objects.all().count()
    return render(request, 'trips/home.html', {'trips_count':trips_count, 'places_count':places_count})

def trip(request, id):
    trip = get_object_or_404(Trip, id=id)
    return render(request, 'trips/trip.html', {'trip':trip})

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

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(trip__title__istartswith=search)
            )
        return queryset
