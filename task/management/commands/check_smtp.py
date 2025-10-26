from django.core.management.base import BaseCommand
from resend import Resend
from django.conf import settings

class Command(BaseCommand):
    help = 'Send a test email via Resend'

    def handle(self, *args, **kwargs):
        client = Resend(settings.RESEND_API_KEY)
        client.emails.send(
            from_="dyper777@gmail.com",
            to=["dyper777@gmail.com"],
            subject="Hello from Railway",
            html="<p>This email works!</p>",
        )
        self.stdout.write(self.style.SUCCESS('Email sent!'))
