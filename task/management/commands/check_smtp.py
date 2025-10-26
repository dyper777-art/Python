from django.core.management.base import BaseCommand
import smtplib

class Command(BaseCommand):
    help = "Check SMTP server connectivity"

    def handle(self, *args, **kwargs):
        host = "smtp.gmail.com"
        port = 587

        try:
            server = smtplib.SMTP(host, port, timeout=10)
            server.starttls()
            server.quit()
            self.stdout.write(self.style.SUCCESS(f"SMTP {host}:{port} is reachable!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed to connect: {e}"))
