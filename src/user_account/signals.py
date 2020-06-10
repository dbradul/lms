from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from user_account.models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.profile:
        instance.profile.save()


# @receiver(post_save, sender=User)
# def create_user_profile2(sender, instance, created, **kwargs):
#     if created:
#         UserProfile2.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile2(sender, instance, **kwargs):
#     instance.profile2.save()