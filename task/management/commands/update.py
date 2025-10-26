from django.core.management.base import BaseCommand
from task.models import Category, Tag, Task
from faker import Faker

class Command(BaseCommand):
    help = 'Update Data.'

    def handle(self, *args, **kwargs):

        try:
            faker = Faker()
            rows = Tag.objects.all()

            for row in rows:
                row.rate = faker.random_int(min=1, max=10)
                row.save()

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"\n\n=== Update Error {str(e)} ===\n"))
        else:
            self.stdout.write(self.style.SUCCESS("\n\n=== Update Done ===\n"))


# rate = faker.random_int(min=1, max=10)
# address = faker.address().replace('\n', ', ')
# city = faker.city()
# country = faker.country()
# phone_number = faker.phone_number()
# email = faker.email()

