# from django.core.management.base import BaseCommand
# from django.contrib.auth import get_user_model

# class Command(BaseCommand):
#     help = 'Creates a superuser with only a username.'

#     def handle(self, *args, **kwargs):

#         self.stdout.write(self.style.WARNING(f"\n---= Create Super User =---"))
#         print("Enter username: ", end="", flush=True)
#         username = input().strip()
#         email = f"{username}@gmail.com"
#         password = '123'

#         User = get_user_model()
#         if not User.objects.filter(username=username).exists():
#             User.objects.create_superuser(
#                 username=username,
#                 email=email,
#                 password=password,
#             )
#             self.stdout.write(self.style.SUCCESS(f"Superuser {username}'s password is 123."))
#         else:
#             self.stdout.write(self.style.NOTICE(f"Superuser '{username}' already exists."))

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser with username passed as argument or interactively.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            help='Username for the superuser (if not provided, will prompt)',
        )

    def handle(self, *args, **kwargs):
        username = kwargs.get('username')

        if not username:
            self.stdout.write(self.style.WARNING("\n---= Create Super User =---"))
            self.stdout.write(self.style.WARNING("\n--> Warning <--\nuser name admin already created with password 123.\nChoose Another Name."))
            username = input("\nEnter username: ").strip()

        email = f"{username}@gmail.com"
        password = '123'

        User = get_user_model()
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created with password '{password}'."))
        else:
            self.stdout.write(self.style.NOTICE(f"Superuser '{username}' already exists."))
