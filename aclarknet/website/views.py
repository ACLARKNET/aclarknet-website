from .forms import ContactForm
from .models import Developer
from .models import Partner
from .models import Testimonial
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
import requests

# Create your views here.

CLIENT_URL = 'https://db.aclark.net/api/clients/?format=json'
SERVICE_URL = 'https://db.aclark.net/api/services/?format=json'


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
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'contact.html', context)


def history(request):
    context = {}
    return render(request, 'history.html', context)


def home(request):
    context = {}
    testimonials = Testimonial.objects.order_by('?')
    if testimonials.count() > 0:
        testimonial = testimonials[0]
        context['testimonial'] = testimonial
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
    testimonials = Testimonial.objects.filter(active=True)
    context['testimonials'] = testimonials
    return render(request, 'testimonials.html', context)


def team(request):
    context = {}
    developers = Developer.objects.filter(active=True)
    partners = Partner.objects.filter(active=True)
    context['developers'] = developers
    context['partners'] = partners
    return render(request, 'team.html', context)
