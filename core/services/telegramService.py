import requests
from django.conf import settings

class TelegramService:

    def __init__(self):
        self.BASE_URL = 'https://api.telegram.org/bot'
        self.TOKEN = settings.TG_TOKEN
        self.CHAT_ID = settings.TG_CHAT_ID

    def sendContactNotification(self, name, email, message):
        url = self.BASE_URL + self.TOKEN + '/sendMessage'
        message = f'<b>New Contact Message 📬</b>\nDear lord, you have received a new message from {name} ({email}), the message is the next one:\n\n<pre>{message}</pre>'
        payload = {'chat_id': self.CHAT_ID, 'parse_mode': 'HTML', 'text': message }
        r = requests.post(url, json=payload, timeout=5.0)
        print(r.status_code)
        print(r.text)
        return r.status_code == requests.codes.ok

