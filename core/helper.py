from django.conf import settings
from django.core.mail import send_mail

def mail(to,subject,message):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [to]
    send_mail( subject, message, email_from, recipient_list )