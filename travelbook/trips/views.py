from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q
from django.views import generic
from .models import Trip, Place, PlaceImage
from .forms import PlaceDescriptionForm


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

# def place_entry_view(request, id):
#     place = get_object_or_404(Place, id=id)
#     descr = PlaceEntry.objects.filter(place=place)
#     return render(request, 'trips/place_entry.html', {'place':place, 'descr':descr, })


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


class PlaceCreateView(generic.CreateView):
    model = Place
    template_name = 'trips/place_entry.html'
    form_class = PlaceDescriptionForm
    success_url = reverse_lazy('home')


class AddPlaceView(generic.CreateView):
    model = Place
    template_name = 'trips/add_place.html'
    fields = '__all__'
    # form_class = PlaceDescriptionForm
    success_url = reverse_lazy('home')


class EditPlaceView(generic.UpdateView):
    model = Place
    template_name = 'trips/edit_place.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('place_list')


class DeletePlaceView(generic.DeleteView):
    model = Place
    template_name = 'trips/delete_place.html'
    success_url = reverse_lazy('place_list')


class AddImagesView(generic.CreateView):
    model = PlaceImage
    template_name = 'trips/add_images.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')

    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['trip'] = self.request.GET.get('trip_id')
    #     initial['name'] = self.request.GET.get('name')
    #     return initial

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     trip_id = self.request.GET.get('trip_id')
    #     if trip_id:
    #         context['trip'] = get_object_or_404(Trip, id=trip_id)
    #     name = self.request.GET.get('name')
    #     if name:
    #         context['name'] = get_object_or_404(Trip, id=name)
    #     return context

    # def form_valid(self, form):
    #     form.instance.place = self.object
    #     # form.instance.reviewer = self.request.user
    #     form.save()
    #     return super(PlaceCreateView, self).form_valid(form)
    