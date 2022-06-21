from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.views import generic
from .models import Trip, Place, PlaceImage
from .forms import TripForm, PlaceDescriptionForm, PlaceImageForm


def index(request):
    return render(request, 'trips/index.html')

def home(request):
    trips_count = Trip.objects.all().count()
    places_count = Place.objects.all().count()
    return render(request, 'trips/home.html', {'trips_count':trips_count, 'places_count':places_count})

def trip(request, id):
    trip = get_object_or_404(Trip, id=id)
    return render(request, 'trips/trip.html', {'trip':trip})


class TripListView(generic.ListView, ModelFormMixin):
    model = Trip
    context_object_name = 'trips'
    template_name = 'trips/trip_list.html'
    form_class = TripForm
    success_url = reverse_lazy('trip_list')

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        return generic.ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        self.form.instance.owner = self.request.user
        if self.form.is_valid():
            self.object = self.form.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(TripListView, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
        return context
        

class DeleteTripView(generic.DeleteView):
    model = Trip
    template_name = 'trips/delete_trip.html'
    success_url = reverse_lazy('trip_list')


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


class PlaceDetailView(generic.DetailView, FormMixin):
    model = Place
    template_name = 'trips/place_details.html'
    form_class = PlaceImageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = PlaceImage.objects.filter(place=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy('place_details', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.place = self.object
        form.save()
        return super().form_valid(form)


class AddPlaceView(generic.CreateView):
    model = Place
    template_name = 'trips/add_place.html'
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return redirect('place_list')


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
    success_url = reverse_lazy('place_list')


    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['trip'] = self.request.GET.get('trip_id')
    #     initial['name'] = self.request.GET.get('name')
    #     return initial
    