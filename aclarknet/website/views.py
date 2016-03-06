from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
import random
import requests

# Create your views here.

CLIENT_URL = 'https://aclarknet-database.herokuapp.com/api/clients/?format=json'
SERVICE_URL = 'https://aclarknet-database.herokuapp.com/api/services/?format=json'
TESTIMONIAL_URL = 'https://aclarknet-database.herokuapp.com/api/testimonials/?format=json'
PROFILE_URL = 'https://aclarknet-database.herokuapp.com/api/profiles/?format=json'


def about(request):
    context = {}
    return render(request, 'about.html', context)


def page(request, slug=None):
    context = {}
    return render(request, 'page.html', context)


def book(request):
    context = {}
    return render(request, 'book.html', context)


def clients(request):
    context = {}
    clients = requests.get(CLIENT_URL).json()
    context['clients'] = clients
    return render(request, 'clients.html', context)


def community(request):
    context = {}
    return render(request, 'community.html', context)


def contact(request):
    context = {}
    now = timezone.datetime.now
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            recipients = [settings.DEFAULT_FROM_EMAIL]
            subject = settings.DEFAULT_SUBJECT % now().strftime(
                '%m/%d/%Y %H:%M:%S')
            send_mail(subject, message, sender, recipients)
            messages.add_message(
                request, messages.INFO,
                'Thank you! Please expect our reply within 24 hours.')
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'contact.html', context)


def history(request):
    context = {}
    return render(request, 'history.html', context)


def home(request):
    context = {}
    testimonials = requests.get(TESTIMONIAL_URL).json()
    context['testimonial'] = random.choice(testimonials)
    return render(request, 'home.html', context)


def location(request):
    context = {}
    return render(request, 'location.html', context)


def open_source(request):
    context = {}
    return render(request, 'open_source.html', context)


def projects(request):
    context = {}
    return render(request, 'projects.html', context)


def services(request):
    context = {}
    services = requests.get(SERVICE_URL).json()
    context['services'] = services
    return render(request, 'services.html', context)


def testimonials(request):
    context = {}
    testimonials = requests.get(TESTIMONIAL_URL).json()
    context['testimonials'] = testimonials
    return render(request, 'testimonials.html', context)


def team(request):
    context = {}
    profiles = requests.get(PROFILE_URL).json()
    context['profiles'] = profiles
    return render(request, 'team.html', context)


def now(request):
    return HttpResponseRedirect('http://blog.aclark.net/now')
