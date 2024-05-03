from django.urls import path, include
from .views import contact
urlpatterns = [
    path('contact/', contact, name="contact_url"),
]