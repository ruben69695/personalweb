from django.shortcuts import render, HttpResponse
from .forms import ContactMessageForm
from .services.emailService import EmailService
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def contact(request):
    return render(request, "core/contact.html")

def aboutMe(request):
    return render(request, 'core/about-me.html')

def createContactMessage(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save()
            fromEmail = settings.DEFAULT_FROM_EMAIL
            subject = new_message.name + ', with email (' + new_message.email + ') needs your attention'
            service = EmailService(fromEmail, [fromEmail], subject, new_message.message)
            service.send()
            
            if service.sended:
                print('Email sended correctly')
    
    return render(request, "core/contact.html")
