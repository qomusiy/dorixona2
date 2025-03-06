from django.urls import path
from .views import Home, Infopill, About, Contact
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('infopill/<int:pk>/', Infopill.as_view(), name='infopill'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
]