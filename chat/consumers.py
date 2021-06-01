import json
from django.utils import timezone

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from chat.models import ConnectedUsers


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'library_chat'
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope['user']

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        ConnectedUsers.objects.create(first_name=self.user.first_name,
                                      last_name=self.user.last_name,
                                      username=self.user.username)
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        ConnectedUsers.objects.filter(first_name=self.user.first_name,
                                      last_name=self.user.last_name,
                                      username=self.user.username).delete()

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.user.username,
                'datetime': timezone.now().isoformat()
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps(event))