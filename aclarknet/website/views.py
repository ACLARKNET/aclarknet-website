from django.shortcuts import render

# Create your views here.


def about(request):
    context = {}
    return render(request, 'about.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def home(request):
    context = {}
    return render(request, 'home.html', context)


def projects(request):
    context = {}
    return render(request, 'projects.html', context)


def services(request):
    context = {}
    return render(request, 'services.html', context)
