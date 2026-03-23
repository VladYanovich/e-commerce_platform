import asyncio
import logging

from src.bot import bot, dp
from src.rabbitmq.broker import broker

# IMPORTANT: registers RabbitMQ handlers
import src.rabbitmq.handlers


async def main():
    async with broker:
        await broker.start()
        logging.info("Broker started")

        await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())