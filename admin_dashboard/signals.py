from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Action

@receiver(post_save)
def track_save(sender, instance, created, **kwargs):
    if not isinstance(instance, Action):  # Prevent recursion
        action = "added" if created else "changed"
        # Check if instance has a user field
        if hasattr(instance, 'user'):
            Action.objects.create(
                user=instance.user,  # Assuming instance has a user field
                action=action,
                content_type=ContentType.objects.get_for_model(sender),
                object_id=instance.pk,
                object_repr=str(instance)
            )

@receiver(post_delete)
def track_delete(sender, instance, **kwargs):
    if not isinstance(instance, Action):  # Prevent recursion
        # Check if instance has a user field
        if hasattr(instance, 'user'):
            Action.objects.create(
                user=instance.user,  # Assuming instance has a user field
                action="deleted",
                content_type=ContentType.objects.get_for_model(sender),
                object_id=instance.pk,
                object_repr=str(instance)
            )
