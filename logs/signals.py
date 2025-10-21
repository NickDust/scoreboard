from django.conf import settings
from django.db.models.signals import post_save, pre_save
from .models import LogModel
from django.dispatch import receiver
from registration.models import UserProfileModel


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_created(sender, instance=None, created=False,**kwargs):
    if created:
        LogModel.objects.create(user=instance, action="USER_CREATED")

@receiver(pre_save, sender=UserProfileModel)
def rank_up(sender, instance=None, created=False, **kwargs):
    if not instance.pk:
        return
    old = UserProfileModel.objects.get(pk=instance.pk)
    if old.rank.rank != instance.rank.rank:
        LogModel.objects.create(user=instance.user, action="RANK_UP")

@receiver(pre_save, sender=UserProfileModel)
def points_added(sender, instance=None, created=False, **kwargs):
    if not instance.pk:
        return
    current_points = UserProfileModel.objects.get(pk=instance.pk)
    if current_points.points != instance.points:
        LogModel.objects.create(user=instance.user, action="POINTS_ADDED")
