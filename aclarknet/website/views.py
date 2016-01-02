from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.utils import timezone
from .forms import ContactForm
import datetime
import os

# Create your views here.


def about(request):
    context = {}
    return render(request, 'about.html', context)


def contact(request):
    context = {}
    now = datetime.datetime.now
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            message2 = form.cleaned_data['message2']
            sender = form.cleaned_data['email']
            recipients = ['info@aclark.net']
            salesforce = os.environ.get('EMAIL_TO_SALESFORCE_ADDRESS')
            subject = 'ACLARK.NET Contact Form Submission %s' % now().strftime(
                '%m/%d/%Y %H:%M:%S')
            send_mail(subject, message + '\n\n' + message2, sender, recipients)
            if salesforce:
                send_mail(subject, message + '\n\n' + message2,
                          'info@aclark.net', [salesforce])
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm()
    context['form'] = form
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
