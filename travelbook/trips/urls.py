from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trip_list/', views.trip_list_view, name='trip_list'),
    path('place_details/<int:id>/', views.place_details_view, name='place_details'),
]
