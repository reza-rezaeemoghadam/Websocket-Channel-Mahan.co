# Importing django modules
from django.db.models.signals import post_save
from django.dispatch import receiver

# Importing channels module
from channels.layers import get_channel_layer

# Importing extra modules
from asgiref.sync import async_to_sync

# Importing custom models
from message_app.models import Message

@receiver(post_save, sender=Message)
def send_message__notification(sender, instance, created, **kwargs):
    if created:
        async_to_sync(send_message)(instance)

async def send_message(instance):
    channel_layer = get_channel_layer()
    await channel_layer.group_send(
        f'company_{instance.company.id}',
        {
            'type':'room_message',
            'message': {'message': instance.body,
                        'color': instance.level,
                        'user': instance.user.id}
        }
    )