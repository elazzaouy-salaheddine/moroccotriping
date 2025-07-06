from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from tour.models import Tour, Enquiry
# Create your views here.
class DashboardViews(TemplateView):
    template_name = 'dashboard/index.html'  # specifies the template to use

class ToursListViews(ListView):
    model = Tour
    template_name = 'dashboard/tours_list.html'
    context_object_name = 'tours'
    paginate_by = 10  # Optional pagination

    def get_queryset(self):
        # Always order by a field to ensure consistent pagination
        return Tour.objects.order_by('-updated_at')  # or '-created_at', etc.



class EnquiriesListViews(ListView):
    model = Enquiry
    template_name = 'dashboard/booking_list.html'
    context_object_name = 'enquiries'
    #paginate_by = 9  # Optional pagination

    def get_queryset(self):
        # Always order by a field to ensure consistent pagination
        return Enquiry.objects.order_by('-created_at')  # or '-created_at', etc.

class EnquiriesDetailsViews(DetailView):
    model = Enquiry
    template_name = 'dashboard/booking_details.html'
    context_object_name = 'enquiry'