from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from pages.models import ContactInfo, HomeSlider
from footerInfo.models import FooterAboutInfo, SocialLinks, FooterLinks
from .forms import ContactForm
from django.views.generic.edit import FormMixin





class HomepageView(TemplateView):
    template_name = 'pages/home.html'  # specifies the template to use
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Us'
        context['home_slider'] = HomeSlider.objects.all()
        return context

def about_us(request):
    return render(request, 'pages/about_us.html')

class ContactView(FormMixin, TemplateView):
    template_name = 'pages/contact_us.html'  # specifies the template to use
    form_class = ContactForm

    meta = {
        'title': 'Contact Us - Tripix Travel',
        'description': 'Learn more about our mission and values at Tripix.',
        'og_description': 'Discover how Tripix is making travel unforgettable.',
        'twitter_title': 'Contact | Tripix',
        'keywords': ['travel', 'contact us', 'Tripix', 'tour guide'],
    }
    def get_success_url(self):
        return reverse('home')

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
        context['title'] = 'Contact Us'
        context['contact_info'] = 'Feel free to reach out to us!'
        context['contacts'] = ContactInfo.objects.all()
        context['form'] = self.get_form() 
        return context

def TermsandCondition(request):
    return render(request, 'pages/terms_condition.html')

def PrivacyPolicy(request):

    return render(request, 'pages/privacy_policy.html')