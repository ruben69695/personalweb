from django.shortcuts import render, HttpResponse
from .forms import ContactMessageForm
from .services.emailService import EmailService
from .services.telegramService import TelegramService
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
            email_service = EmailService(fromEmail, [fromEmail], subject, new_message.message)
            email_service.send()
            
            if email_service.sended:
                print('Email sended correctly')

            if settings.TG_ACTIVE:
                tg_service = TelegramService()
                sent_ok = tg_service.sendContactNotification(new_message.name, new_message.email, new_message.message)
                if sent_ok:
                    print('Telegram notification sended correctly')
    
    return render(request, "core/contact.html")
