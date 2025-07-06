from django.contrib import admin
from .models import Tour, Tag,Enquiry, TopTour, GalleryImage,Destination
from django.utils.html import format_html




class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1
    max_num = 10  # Limits inline formset to 10 images
admin.site.register(Destination)

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'duration_days', 'price')
    search_fields = ('name', 'location', 'overview')
    list_filter = ('tags', 'location', 'duration_days')
    prepopulated_fields = {'slug': ('name',)}  # only if you add a slug field



    fieldsets = (
        (None, {
            'fields': ('created_by','destination','name', 'image', 'overview', 'slug')
        }),
        ('Details', {
            'fields': ('location', 'accommodation', 'best_season', 'duration_days', 'elevation', 'tour_types','old_price', 'price')
        }),
        ('Tags', {
            'fields': ('tags',)
        }),
    )

    inlines = [
        GalleryImageInline,
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'tour', 'created_at')
    list_filter = ('tour', 'created_at')
    readonly_fields = ('created_at',)

admin.site.register(TopTour)
