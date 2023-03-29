import asyncio
from rabbit_client import RabbitClient


async def start_send():
    async with RabbitClient() as connection:
        await RabbitClient.put(connection=connection,
                               message_data="23dfsdfsdfdsffsadfsddsadfsa",
                               queue_name='hello')


async def start_resive():
    async with RabbitClient() as connection:
        await RabbitClient.receive(connection=connection,
                                   queue_name='hello', )


if __name__ == "__main__":
    asyncio.run(start_send())
    asyncio.run(start_resive())
