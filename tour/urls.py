# core/urls.py

from django.urls import path
from .views import TourListView, TourDetailView, DetinationsView,ToursByDetinationView

urlpatterns = [
    path('', TourListView.as_view(), name='tours-list'),
    path('destinations/', DetinationsView.as_view(), name='destinations-list'),
    path('<slug:slug>/', TourDetailView.as_view(), name='tour-detail'),
    path('destinations/<slug:slug>/', ToursByDetinationView.as_view(), name='tours-by-destination'),


    #path('<int:pk>/', DestinationDetailView.as_view(), name='destination-detail'),
    #path('thank-you/', thank_you, name='thank_you'),

]