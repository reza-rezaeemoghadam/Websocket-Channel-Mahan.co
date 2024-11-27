# Importing channels module
from channels.generic.websocket import AsyncWebsocketConsumer

# Importing extra modules
import json
from asgiref.sync import async_to_sync

class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        
        self.company_id = self.scope['url_route']['kwargs']['company_id']
        self.company_group_name = f'company_{self.company_id}'
        print(self.company_id)
        await self.channel_layer.group_add(
            self.company_group_name,
            self.channel_name
        )
        await self.accept()        
        await self.send(text_data=json.dumps({
            'message': f'Connected to group: {self.company_group_name}'
        }))
    
    async def disconnect(self, code):
        print(f"Message received: disconnected")
        return super().disconnect(code)
    
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(f"Message received: {message}")
        await self.channel_layer.group_send(
            self.company_group_name,
            {
                'type': 'room_message',
                'message': message,
            }
        )
    
    async def room_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'type':'chat',
            'message': message,
        }))