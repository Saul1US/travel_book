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
    path('delete_place/<int:pk>/', views.DeletePlaceView.as_view(), name='delete_place'),
    path('add_images/<int:pk>/', views.AddImagesView.as_view(), name='add_images'),
    path('place_entry/<int:id>/', views.PlaceCreateView.as_view(), name='place_entry'),
    path('place_details/<int:pk>/', views.PlaceDetailView.as_view(), name='place_details'),
]
