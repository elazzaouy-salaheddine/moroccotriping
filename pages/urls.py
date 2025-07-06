from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomepageView.as_view(), name="home"),
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', views.ContactView.as_view(), name='contact-us'),
    path('terms-condition/', views.TermsandCondition, name='terms-condition'),
    path('privacy-policy/', views.PrivacyPolicy, name='privacy-policy'),
]
