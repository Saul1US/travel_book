from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    # path('trip_list/', views.trip_list_view, name='trip_list'),
    path('trip/<int:id>', views.trip, name='trip'),
    path('trip_list/', views.TripListView.as_view(), name='trip_list'),
    path('place_list/', views.PlaceListView.as_view(), name='place_list'),
    path('place_details/<int:id>/', views.place_details_view, name='place_details'),
]
