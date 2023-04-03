import asyncio


from app_rabbitMQ.rabbit_client import RabbitClient


async def start_send(message):
    async with RabbitClient() as connection:
        await RabbitClient.put(connection=connection,
                               message_data=message,
                               queue_name='hello')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(start_send('glhgjhg'))
    loop.run_forever()