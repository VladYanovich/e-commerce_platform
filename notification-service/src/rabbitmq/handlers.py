from faststream.rabbit import RabbitExchange, RabbitQueue, ExchangeType

from src.bot import bot
from src.config import settings
from src.rabbitmq.broker import broker

product_exchange = RabbitExchange(
    "product_events",
    type=ExchangeType.TOPIC,
    durable=True,
)

product_queue = RabbitQueue(
    "notification_product_created",
    durable=True,
    routing_key="product.created",
)


@broker.subscriber(queue=product_queue, exchange=product_exchange)
async def handle_products(data: dict):
    event = data.get("event", "unknown")
    product = data.get("product", {})

    text = (
        f"🔔 {event}\n\n"
        f"📦 {product.get('name')}\n"
        f"💰 {product.get('price')} {product.get('currency')}\n"
        f"📝 {product.get('description')}"
    )

    await bot.send_message(
        chat_id=settings.telegram.channel_id,
        text=text,
    )