from django.shortcuts import render, redirect
from .forms import ContactForm  

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # կամ վերաhդարձրու success հաղորդագրություն
    else:
        form = ContactForm()
    return render(request, 'home.html', { 'form': form})


def News(request):
    return render(request, 'news.html', {})
