from django.core.management.base import BaseCommand
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Command(BaseCommand):
    help = 'Test Redis connection through channel layer'

    def handle(self, *args, **kwargs):
        channel_layer = get_channel_layer()

        # Send a test message to a channel
        try:
            async_to_sync(channel_layer.send)('test_channel', {'type': 'test.message', 'text': 'Hello, Redis!'})
            self.stdout.write(self.style.SUCCESS('Message sent to test_channel'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error sending message: {e}'))
            return

        # Receive the test message from the channel
        try:
            response = async_to_sync(channel_layer.receive)('test_channel')
            self.stdout.write(self.style.SUCCESS(f'Received message: {response["text"]}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error receiving message: {e}'))
