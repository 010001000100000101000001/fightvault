from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Contact form view
def contact_view(request):
    return render(request, 'contact/contact.html')


def send_email_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        subject = 'FightVault Contact Form'
        email_message = f'From: {email}\n\n{message}'

        # Send email using send_mail function
        send_mail(
            subject,
            email_message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER]
        )

        return HttpResponseRedirect(reverse('thank_you'))

    # Redirect to contact_view if accessed via GET
    return redirect('contact_view')


def thank_you_view(request):
    return render(request, 'contact/thank_you.html')
