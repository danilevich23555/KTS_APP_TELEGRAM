import asyncio

from app_rabbitMQ.rabbit_client import MetaclassWorker



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(MetaclassWorker.handler())
    loop.run_forever()