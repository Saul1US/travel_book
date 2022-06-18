from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('trip/<int:id>', views.trip, name='trip'),
    path('trip_list/', views.TripListView.as_view(), name='trip_list'),
    path('place_list/', views.PlaceListView.as_view(), name='place_list'),
    path('add_place/', views.AddPlaceView.as_view(), name='add_place'),
    path('edit_place/<int:pk>/', views.EditPlaceView.as_view(), name='edit_place'),
    path('place_entry/<int:id>/', views.PlaceCreateView.as_view(), name='place_entry'),
    path('place_details/<int:id>/', views.place_details_view, name='place_details'),
]
