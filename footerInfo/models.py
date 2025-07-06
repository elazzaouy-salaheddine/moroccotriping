from django.db import models

# Create your models here.
class FooterAboutInfo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    Address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class SocialLinks(models.Model):
    name = models.CharField(max_length=30)
    icone_class = models.CharField(max_length=30)
    link = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class FooterLinks(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=30)
    space_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name