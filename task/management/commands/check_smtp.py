from django.core.management.base import BaseCommand
import os
import resend

class Command(BaseCommand):
    help = 'Send a test email via Resend'

    def handle(self, *args, **kwargs):
        # Set API key
        resend.api_key = os.environ.get("RESEND_API_KEY")

        params = {
            "from": "Acme <onboarding@resend.dev>",  # or your verified domain
            "to": ["dyper777@gmail.com"],
            "subject": "Hello from Railway",
            "html": "<p>This email works!</p>",
        }

        email = resend.Emails.send(params)

        # Access dictionary keys instead of attributes
        self.stdout.write(self.style.SUCCESS(f'Email sent! ID: {email["id"]}'))
        self.stdout.write(self.style.SUCCESS(f'Status: {email["status"]}'))
