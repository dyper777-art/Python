from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
import uuid

class Command(BaseCommand):
    help = "Send a verification email using Gmail SMTP"

    def add_arguments(self, parser):
        parser.add_argument("--to", type=str, required=True, help="Recipient email")

    def handle(self, *args, **options):
        recipient = options["to"]

        # Generate a unique token (you can store this in DB if needed)
        token = uuid.uuid4()
        verification_link = f"http://127.0.0.1:8000/api/verify-email/{token}/"

        subject = "Verify Your Email Address"
        message = (
            f"Hello,\n\n"
            f"Please verify your email by clicking this link:\n{verification_link}\n\n"
            f"If you didn’t request this, ignore this email.\n\n"
            f"-- Django App"
        )

        self.stdout.write(self.style.WARNING(f"Sending verification email to {recipient}"))

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient],
                fail_silently=False,
            )
            self.stdout.write(self.style.SUCCESS("Verification email sent successfully!"))
            # self.stdout.write(self.style.HTTP_INFO(f"Token: {token}"))  # optional
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed to send email: {e}"))
