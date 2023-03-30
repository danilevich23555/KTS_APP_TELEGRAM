import asyncio
from app_rabbitMQ.rabbit_client import RabbitClient


async def start_send(message):
    async with RabbitClient() as connection:
        await RabbitClient.put(connection=connection,
                               message_data=message,
                               queue_name='hello')


async def start_resive():
    async with RabbitClient() as connection:
        await RabbitClient.receive(connection=connection,
                                   queue_name='hello', )



if __name__ == '__main__':
    asyncio.run(start_resive())
    asyncio.run(start_resive())