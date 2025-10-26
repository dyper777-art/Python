from django.core.management.base import BaseCommand
import os
import resend

class Command(BaseCommand):
    help = 'Send a test email via Resend'

    def handle(self, *args, **kwargs):
        # Set your API key
        resend.api_key = os.environ.get("RESEND_API_KEY")

        # Prepare email params
        params: resend.Emails.SendParams = {
            "from": "Acme <onboarding@resend.dev>",
            "to": ["dyper777@gmail.com"],
            "subject": "Hello from Railway",
            "html": "<p>This email works!</p>",
        }

        # Send the email
        email = resend.Emails.send(params)
        self.stdout.write(self.style.SUCCESS(f'Email sent! ID: {email.id}'))
