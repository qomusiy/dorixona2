from django.shortcuts import render
from .models import Pills
from django.views import View


# Create your views here.
# def home(request):
#     return render(request, template_name='home.html', context={'pill':Pills.objects.all()})

class Home(View):
    def get(self, request):
        return render(request, template_name='home.html', context={'pill':Pills.objects.all()})

# def infopill(request, pk):
#     return render(request, template_name='infopill.html', context={'pill':Pills.objects.get(id=pk)})

class Infopill(View):
    def get(self, request, pk):
        return render(request, template_name='infopill.html', context={'pill':Pills.objects.get(id=pk)})

# def about(request):
#     return render(request, template_name='about.html')

class About(View):
    def get(self, request):
        return render(request, template_name='about.html')

# def contact(request):
#     return render(request, template_name='contact.html')

class Contact(View):
    def get(self, request):
        return render(request, template_name='contact.html')