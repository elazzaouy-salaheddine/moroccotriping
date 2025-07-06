from django.views.generic import ListView, DetailView
from .models import Tour, Destination
from django.shortcuts import render, redirect
from django.views.generic.edit import FormMixin
from django.urls import reverse
from .forms import EnquiryForm




class TourListView(ListView):
    model = Tour
    template_name = 'tours/tour_list.html'
    context_object_name = 'tours'
    #paginate_by = 9  # Optional pagination

    def get_queryset(self):
        return Tour.objects.order_by('-updated_at')  # or '-created_at', etc.
    

class TourDetailView(FormMixin, DetailView):
    model = Tour
    template_name = 'tours/tour_details.html'
    context_object_name = 'tour'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    form_class = EnquiryForm
    def get_success_url(self):
        return reverse('tours-list')

    def get_initial(self):
        initial = super().get_initial()
        initial['tour'] = self.object.id
        return initial

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.tour = self.object
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form() 
        return context
    

def thank_you(request):
    return render(request, 'tours/thank_you.html')




class DetinationsView(ListView):
    model = Destination
    template_name = 'destinations/destinations_list.html'
    context_object_name = 'destinations'
    #paginate_by = 9  # Optional pagination

    def get_queryset(self):
        return Destination.objects.order_by('-created_at')  # or '-created_at', etc.
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    
class ToursByDetinationView(ListView):
    model = Tour
    template_name = 'tours/tour_list.html'
    context_object_name = 'tours'
    #paginate_by = 6

    def get_queryset(self):
        return Tour.objects.filter(
            destination__slug=self.kwargs['slug'],
            published=True
        ).order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Tours by Destination: {Destination.objects.get(slug=self.kwargs['slug']).name}"
        return context
