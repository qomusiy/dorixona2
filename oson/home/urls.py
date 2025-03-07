from django.urls import path
from .views import Home, Infopill, About, Contact, Addpill, Editpill, Deletepill
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('infopill/<int:pk>/', Infopill.as_view(), name='infopill'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('addpill/', Addpill.as_view(), name='addpill' ),
    path('edit/<int:pk>/', Editpill.as_view(), name='edit'),
    path('delete/<int:pk>/', Deletepill.as_view(), name='delete')
]