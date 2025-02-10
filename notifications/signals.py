# notifications/signals.py
from django.dispatch import receiver
from django.db.models.signals import post_save
from chat.models import Message  # assuming you have a Message model (or use ChatConsumer’s events)
from notifications.models import Notification

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        job_poster = instance.room.job.employer  # adjust based on your Room/Job relation
        Notification.objects.create(
            recipient=job_poster,
            verb=f"{instance.sender.username} sent you a message.",
            target_url=f"/chat/room/{instance.room.id}/"
        )
