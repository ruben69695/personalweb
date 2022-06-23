from django.core import mail
from django.core.mail import send_mail

class EmailService():

    def __init__(self, fromMail, recipient_list, subject, message):
        self.fromMail = fromMail
        self.recipient_list = recipient_list
        self.subject = subject
        self.message = message
        self.sended = False
    
    def send(self):
        emailBackend = mail.get_connection()
        result = send_mail(self.subject, self.message, self.fromMail, self.recipient_list, False, connection=emailBackend)
        self.sended = result == 1
