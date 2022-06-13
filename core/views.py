from django.shortcuts import render, HttpResponse
from .forms import ContactMessageForm
from .services.emailService import EmailService

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
            subject = new_message.name + ' needs your attention'
            service = EmailService(new_message.email, ['ruben.arre6@gmail.com'], subject, new_message.message)
            service.send()
            
            if service.sended:
                print('Email sended correctly')
    
    return render(request, "core/contact.html")