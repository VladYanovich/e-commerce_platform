from faststream.rabbit import RabbitBroker, RabbitExchange, ExchangeType

from src.core.config import settings

broker = RabbitBroker(settings.rabbitmq.url)

product_exchange = RabbitExchange(
    "product_events",
    type=ExchangeType.TOPIC,
    durable=True,
)

product_created_publisher = broker.publisher(
    exchange=product_exchange,
    routing_key="product.created",
)

