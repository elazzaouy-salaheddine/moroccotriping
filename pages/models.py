from django.db import models
from tour.models import Destination,Tour


class HomeSlider(models.Model):
    backgourndImage = models.ImageField(upload_to='homeslider/', blank=True, null=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

class HomeTourFacilites(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    home_image = models.ImageField(upload_to='hometour/', blank=True, null=True)
    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    email_1 = models.EmailField()
    email_2 = models.EmailField()
    phone_number_1 = models.CharField(max_length=15, blank=True)
    phone_number_2 = models.CharField(max_length=15, blank=True)
    Opening_Time = models.CharField(max_length=200)
    Location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"