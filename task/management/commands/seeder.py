from django.core.management.base import BaseCommand
from task.models import Task, Category, Tag
from faker import Faker
import random

from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Seed the database with dummy Task data'

    def handle(self, *args, **kwargs):
        faker = Faker()
        categories = list(Category.objects.all())
        tags = list(Tag.objects.all())

        User = get_user_model()
        try:
            user = User.objects.get(username='admin')  # Get User instance here
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("User 'admin' does not exist. Please create it first."))
            return


        if not categories or not tags:
            self.stdout.write(self.style.ERROR('Please ensure you have categories and tags in the database.'))
            return

        for i in range(20):
            try:
                due_date = faker.date_between(start_date='today', end_date='+30d')
                
                task_data = {
                    "name": faker.sentence(nb_words=4),
                    "note": faker.text(max_nb_chars=100),
                    "due_date": due_date,
                    "category": random.choice(categories),
                    "user": user
                }

                task = Task.objects.create(**task_data)

                task.tag.set(random.sample(tags, random.randint(1, len(tags))))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error creating task {i}: {e}"))

        self.stdout.write(self.style.SUCCESS('20 Dummy tasks created successfully!'))
