from typing import Type, Any
from types import TracebackType
from aio_pika import connect, Message
from app_rabbitMQ.settings import settings

print(settings.rabbit_dsn)
class RabbitClient:

    def __init__(self):
        self.connect_rabbit: connect = connect(url=settings.rabbit_dsn,)

    @staticmethod
    async def put(connection: connect, message_data: Any, queue_name: str):
        # Creating a channel
        channel = await connection.channel()
        # Declaring queue
        await channel.declare_queue(queue_name)
        # Sending the message
        await channel.default_exchange.publish(
            Message(str(message_data).encode()),
            routing_key=queue_name,
        )

    @staticmethod
    async def receive(connection: connect, queue_name: str):
        temp = []
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=5)
        queue = await channel.declare_queue(queue_name)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    temp.append(message.body.decode())
        return temp

    async def __aenter__(self) -> connect:
        return await self.connect_rabbit

    async def __aexit__(self, exc_type: Type[BaseException] | None, exc: BaseException | None,
                        tb: TracebackType | None):
        self.connect_rabbit.close()
