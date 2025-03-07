from django.shortcuts import render, redirect
from .models import Pills
from django.views.generic import View, UpdateView, DeleteView
from .forms import PillForm
from django.urls import reverse_lazy


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
    

class Addpill(View):
    def get(self, r):
        return render(r, template_name='addpill.html', context={'form':PillForm()})
    
    def post(self, r):
        form = PillForm(r.POST, r.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(r, template_name='addpill.html', context={'form':form})
    

class Editpill(UpdateView):
    model = Pills
    template_name = 'edit.html'
    form_class = PillForm
    context_object_name = 'pill'

    def get_success_url(self):
        return reverse_lazy('infopill', kwargs={'pk': self.object.pk})
    

class Deletepill(DeleteView):
    model = Pills
    success_url = reverse_lazy('home')
    template_name = 'delete.html'
    context_object_name = 'pill'