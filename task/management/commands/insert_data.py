from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Inserts Data.'

    def handle(self, *args, **kwargs):

        commands = {
            'Make Migrations' : ['makemigrations'],
            'Migrate Database' : ['migrate'],
            'Create Admin' : ['csu','--username', 'admin'],
            'Fixtures Category' : ['loaddata', 'category.json'],
            'Fixtures Tag' : ['loaddata', 'tag.json'],
            'Seeder' : ['seeder'],
        }

        try:
            for label, command in commands.items():
                self.stdout.write(self.style.WARNING(f"\n---= {label} =---"))
                call_command(*command)

        except Exception as e:
            self.stdout.write(self.style.ERROR("Insert Data Error."))
        else:
            self.stdout.write(self.style.SUCCESS("Insert Data Done."))