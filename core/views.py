import logging
from django.shortcuts import render, HttpResponse
from .forms import ContactMessageForm
from .services.emailService import EmailService
from .services.telegramService import TelegramService
from .models import BlacklistedWord
from django.conf import settings

logger = logging.getLogger(__name__)

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

            # Before send check if message has to be banned
            blacklist = BlacklistedWord.objects.all()
            words = request.POST['name'].split() + request.POST['email'].split() + request.POST['message'].split()
            banned, word, blackWord = _blacklistedWordFound(words, blacklist)

            if not banned:
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
            else:
               logger.warning(f'A contact message has been banned, reason: detected a black listed word (w={word},bw={blackWord})') 
    
    return render(request, "core/contact.html")

def _blacklistedWordFound(words: list, blacklistedWords: list):
    found = False
    word = ''
    blackWord = ''
    i = 0

    while not found and i < len(words):

        word = words[i]
        j = 0

        while not found and j < len(blacklistedWords):

            blackWord = blacklistedWords[j].word
            found = _findMatch(word, blackWord)
            j += 1

        i += 1

    return (found, word, blackWord)

def _findMatch(word: str, blackWord: str):
    return word.lower().strip() == blackWord.lower().strip()
