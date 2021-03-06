from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('trip/<int:id>', views.trip, name='trip'),
    path('trip_list/', views.TripListView.as_view(), name='trip_list'),
    path('delete_trip/<int:pk>/', views.DeleteTripView.as_view(), name='delete_trip'),
    path('place_list/', views.PlaceListView.as_view(), name='place_list'),
    path('add_place/', views.AddPlaceView.as_view(), name='add_place'),
    path('edit_place/<int:pk>/', views.EditPlaceView.as_view(), name='edit_place'),
    path('delete_place/<int:pk>/', views.DeletePlaceView.as_view(), name='delete_place'),
    path('place_details/<int:pk>/', views.PlaceDetailView.as_view(), name='place_details'),
    path('my_place_list/', views.UserPlaceListView.as_view(), name='my_place_list'),
]
