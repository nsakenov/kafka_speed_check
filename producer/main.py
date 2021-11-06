"""Produce fake transactions into a Kafka topic."""
import os
import json
from kafka import KafkaProducer, KafkaConsumer
import asyncio
import websockets

Host = "0.0.0.0"

TOPIC_CURRENT_SPEED = os.environ.get('TOPIC_CURRENT_SPEED')
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')

#kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER_URL,
    # Encode all values as JSON
    value_serializer=lambda value: json.dumps(value).encode(),
)

async def time(websocket, path):
    while True:
        speed = await websocket.recv()
        speed = int(speed)
        producer.send(TOPIC_CURRENT_SPEED, value={'speed': speed})
        await asyncio.sleep(1)

async def main():
    async with websockets.serve(time, Host, 8000):
        await asyncio.Future()  # run forever

asyncio.run(main())