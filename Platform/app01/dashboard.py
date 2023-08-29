from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from app01.models import *
import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from COMPATIBILITY.models import *
from django.db.models import Count


class Chart(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        asyncio.ensure_future(self.send_data_loop())

    async def send_data_loop(self):
        while True:
            router_count = Router.objects.count()  # 路由器数量
            compatibility_case = IOT.objects.filter(status=False).values('case').annotate(Count('id')).order_by('-id__count')
            # Profile.objects.values('age').annotate(Count('age'))
            iot_data = dict()
            for i in range(len(compatibility_case)):
                iot_data[compatibility_case[i].get('case')] = compatibility_case[i].get('id__count')
            # print(iot_data)
            # print(router_count)
            data = {'router_count': router_count,
                    'iot_data': iot_data,
                    }
            await self.send(json.dumps(data))
            await asyncio.sleep(1)

    async def disconnect(self, close_code):
        # 连接断开时的逻辑
        pass



# class Chart(WebsocketConsumer):
#     def websocket_connect(self, message):
#         # 有客户端来向后端发送websocket连接的请求时，自动触发
#         # 服务端允许客户端创建连接
#         self.accept()
#         # 服务端主动向客户端推送消息
#         router_count = Router.objects.count()  # 获取所有路由器数量
#         self.send(str(router_count))
#
#     def websocket_receive(self, message):   # 必须要客户端那边先发起send，然后才调用
#         print("接收到消息--->", message)
#         # self.send("XXXX")
#
#     def websocket_disconnect(self, message):
#         raise StopConsumer()
