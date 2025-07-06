from django.db import models
from django.utils.text import slugify
import uuid
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.exceptions import ValidationError


User = get_user_model()

# Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Tag Model
class Destination(models.Model):
    name = models.CharField(max_length=100, unique=True,default='morocco')
    slug = models.SlugField(unique=True, blank=True, null=True)

    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + '-' + str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)



# Destination Model
class Tour(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='tours/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='tours')  # ManyToMany relation
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    accommodation = models.CharField(max_length=255, blank=True, null=True)
    best_season = models.CharField(max_length=255, blank=True, null=True)
    duration_days = models.IntegerField(blank=True, null=True)
    elevation = models.CharField(max_length=100, blank=True, null=True)
    tour_types = models.CharField(max_length=255, blank=True, null=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def included_cost_items(self):
        return self.cost_items.filter(is_included=True)

    @property
    def excluded_cost_items(self):
        return self.cost_items.filter(is_included=False)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + '-' + str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)


# Enquiry Form Submission
class Enquiry(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    Country = models.CharField(max_length=100, blank=True, null=True)
    NoofAdults = models.IntegerField(blank=True, null=True)
    NoofChildren = models.IntegerField(blank=True, null=True)
    EnquirySubject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry from {self.name}"
    

class TopTour(models.Model):
    Tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, blank=True)
    label = models.CharField(max_length=255, blank=True, help_text="e.g., Best Seller, Popular")

    class Meta:
        ordering = ['order']
        verbose_name = 'Top Tour'
        verbose_name_plural = 'Top Tours'

    def __str__(self):
        return f"{self.tour.name} - {self.label or 'Featured'}"

class GalleryImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='tour_galleries/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.tour.name}"

    def save(self, *args, **kwargs):
        # Check if adding this image exceeds 10
        if self.tour.gallery_images.count() >= 10 and not self.pk:
            raise ValidationError("A destination cannot have more than 10 images in the gallery.")
        super().save(*args, **kwargs)