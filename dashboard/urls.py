from django.urls import path
from .views import (
    DashboardViews,ToursListViews,EnquiriesListViews, EnquiriesDetailsViews
)



urlpatterns = [
    path("", DashboardViews.as_view(), name="dashboard"),
    path("tours-list", ToursListViews.as_view(), name="dashboard-tours-list"),
    path("enquiries-list", EnquiriesListViews.as_view(), name="dashboard-enquiries-list"),
    path("enquiries-list/<int:pk>/", EnquiriesDetailsViews.as_view(), name="dashboard-enquiries-details"),

]
