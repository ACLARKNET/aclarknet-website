from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .forms import ContactForm
from .models import Client
from .models import TeamMember
from .models import Testimonial
import datetime
import os

# Create your views here.


def about(request):
    context = {}
    return render(request, 'about.html', context)


def book(request):
    context = {}
    return render(request, 'book.html', context)


def clients(request):
    context = {}
    clients = Client.objects.all()
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
            subject = 'ACLARK.NET, LLC Contact Form Submission %s' % now(
            ).strftime('%m/%d/%Y %H:%M:%S')
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'contact.html', context)


def home(request):
    context = {}
    return render(request, 'home.html', context)


def open_source(request):
    context = {}
    return render(request, 'open_source.html', context)


def projects(request):
    context = {}
    return render(request, 'projects.html', context)


def services(request):
    context = {}
    return render(request, 'services.html', context)


def testimonials(request):
    context = {}
    testimonials = Testimonial.objects.all()
    context['testimonials'] = testimonials
    return render(request, 'testimonials.html', context)


def team(request):
    context = {}
    members = TeamMember.objects.all()
    context['members'] = members
    return render(request, 'team.html', context)
