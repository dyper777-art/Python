# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

# alter warning 
@receiver(post_save, sender=User)
def create_profile_for_superuser(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        Profile.objects.get_or_create(user=instance)
        if not instance.profile.phone:
            print("\n Remember to set a phone number for this superuser!\n")
