from django.urls import path
from .views import home, infopill, about, contact
urlpatterns = [
    path('', home, name='home'),
    path('infopill/<int:pk>/', infopill, name='infopill'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]