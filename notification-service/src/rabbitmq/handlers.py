from faststream.rabbit import RabbitExchange, RabbitQueue, ExchangeType

from src.schemas import ProductCreate
from src.bot import bot
from src.config import settings
from src.rabbitmq.broker import broker
from src.enums import NotificationQueue

product_exchange = RabbitExchange(
    "product_events",
    type=ExchangeType.TOPIC,
    durable=True,
)

product_queue = RabbitQueue(
    NotificationQueue.product_created.value,
    durable=True,
    routing_key="product.created",
)


@broker.subscriber(queue=product_queue, exchange=product_exchange)
async def handle_products(product: dict):
    product = ProductCreate(**product)

    text = (
        f"🔔 {product.event}\n\n"
        f"📦 {product.product.name}\n"
        f"💰 {product.product.price} {product.product.currency}\n"
        f"📝 {product.product.description}"
    )

    await bot.send_message(
        chat_id=settings.telegram.channel_id,
        text=text,
    )