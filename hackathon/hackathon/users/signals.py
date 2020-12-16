from django.db.models.signals import post_save # signal to send
from django.contrib.auth.models import User #sending the signal
from django.dispatch import receiver # receives sig
from .models import Profile


@receiver(post_save, sender=User) # when a user is saved, send signal
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) # run everytime a user is created

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
