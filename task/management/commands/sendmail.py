from django.core.management.base import BaseCommand
import os
import uuid
import resend
from django.conf import settings

class Command(BaseCommand):
    help = "Send a verification email using Resend (Railway-ready)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--to",
            type=str,
            required=True,
            help="Recipient email address",
        )

    def handle(self, request, *args, **options):
        recipient = options["to"]

        # Generate a unique verification token (store in DB if needed)
        token = str(uuid.uuid4())

        # Railway: get host from environment, fallback to Railway deployment URL or localhost
        verification_path = f"/api/verify/{token}/"
        verification_url = request.build_absolute_uri(verification_path) if request else f"{verification_path}"

        # Prepare email content
        subject = "Verify Your Email Address"
        html_content = (
            f"<p>Hello,</p>"
            f"<p>Please verify your email by clicking this link:</p>"
            f"<p><a href='{verification_url}'>{verification_url}</a></p>"
            f"<p>If you didn’t request this, ignore this email.</p>"
            f"<p>-- Django App</p>"
        )

        # Set Resend API key from Railway environment variable
        resend.api_key = os.environ.get("RESEND_API_KEY")

        self.stdout.write(self.style.WARNING(f"Sending verification email to {recipient}"))

        try:
            # Send email via Resend
            params = {
                "from": "Acme <onboarding@resend.dev>",  # Must be a verified domain/email
                "to": settings.EMAIL_HOST_USER,
                "subject": subject,
                "html": html_content,
            }
            email = resend.Emails.send(params)

            # Access dictionary key for ID
            self.stdout.write(self.style.SUCCESS(f"Verification email sent! ID: {email['id']}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed to send email: {e}"))
