# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        await self.channel_layer.group_add("master", self.channel_name)

        user = self.scope['user']
        print(user)
        user_group = "user_" + str(user.id)
        print(user_group)

        if user.is_authenticated:
            print('User is authenticated')
            await self.channel_layer.group_add(user_group, self.channel_name)
        else:
            print('User is not authenticated')

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)

        user = self.scope['user']
        user_group = "user_" + str(user.id)

        # ....some code..., e.g.:
        message_all = '[All] -- %s' % message

        message_user = '[User] --  %s' % message

        await self.channel_layer.group_send(
            "master", {
                'type': 'master.broadcast',
                'text': message_all
            }
        )

        await self.channel_layer.group_send(
            user_group, {
                'type': 'user.broadcast',
                'text': message_user
            }
        )

    async def master_broadcast(self, event):
        await self.send(text_data=json.dumps({
            'message': event['text']
        }))

    async def user_broadcast(self, event):
        await self.send(text_data=json.dumps({
            'message': event['text']
        }))
