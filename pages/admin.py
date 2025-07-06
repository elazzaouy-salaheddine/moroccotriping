from django.contrib import admin
from .models import ContactMessage,ContactInfo,HomeSlider,HomeTourFacilites
from tour.models import Destination,Tour

class TourHomeInline(admin.TabularInline):
    model = Tour
    extra = 1
    fields = ('name', 'destination')



@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(HomeTourFacilites)
class HomeTourFacilitesAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email_1', 'phone_number_1', 'Location', 'created_at')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'subject', 'created_at')
    search_fields = ('name', 'phone_number', 'email', 'subject')
    readonly_fields = ('created_at',)