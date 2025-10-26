from django.core.management.base import BaseCommand
from resend import ResendClient  # updated import
from django.conf import settings

class Command(BaseCommand):
    help = 'Send a test email via Resend'

    def handle(self, *args, **kwargs):
        client = ResendClient(api_key=settings.RESEND_API_KEY)  # updated initialization
        client.emails.send(
            from_="dyper777@gmail.com",
            to=["dyper777@gmail.com"],
            subject="Hello from Railway",
            html="<p>This email works!</p>",
        )
        self.stdout.write(self.style.SUCCESS('Email sent!'))
