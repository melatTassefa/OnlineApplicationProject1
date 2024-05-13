from django.urls import path, include
from .views import contact,aboutus,login,registration, college_search
urlpatterns = [
    path('contact/', contact, name="contact_url"),
    path('aboutus/', aboutus, name="aboutus_url"),
    path('login/', login, name="login_url"),
    path('registration/', registration, name="registration_url"),
    path('search/', college_search, name="college_search_url")
]