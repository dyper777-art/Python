from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Alter Field.'

    def handle(self, *args, **kwargs):

        commands = {
            'Make Migrations' : ['makemigrations'],
            'Migrate Database' : ['migrate'],
        }

        try:
            for command in commands.values():
                call_command(*command)

        except Exception as e:
            self.stdout.write(self.style.ERROR("Alter Field Error."))