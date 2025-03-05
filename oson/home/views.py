from django.shortcuts import render
from .models import Pills
# Create your views here.
def home(request):
    return render(request, template_name='home.html', context={'pill':Pills.objects.all()})

def infopill(request, pk):
    return render(request, template_name='infopill.html', context={'pill':Pills.objects.get(id=pk)})

def about(request):
    return render(request, template_name='about.html')

def contact(request):
    return render(request, template_name='contact.html')