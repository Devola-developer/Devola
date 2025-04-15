from django.shortcuts import render, redirect
from .models import Service, Portfolio
from .forms import ContactForm  

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # սա կստեղծենք
    else:
        form = ContactForm()
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    return render(request, 'home.html', {'services': services, 'portfolios': portfolios, 'form': form})


def about(request):
    return render(request, 'index.html', {})

def News(request):
    return render(request, 'news.html', {})
