from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Inserts Data.'

    def handle(self, *args, **kwargs):

        try:

            call_command('insert_data')

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"\n\n=== Setup Error {str(e)} ===\n"))
        else:
            self.stdout.write(self.style.SUCCESS("\n\n=== Setup Done ===\n"))

