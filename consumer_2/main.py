import os
from time import sleep
import json
from kafka import KafkaConsumer
import asyncio
import websockets

Host = "0.0.0.0"

TOPIC_SPEED_CHECK = os.environ.get('TOPIC_SPEED_CHECK')
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')

consumer = KafkaConsumer(
    TOPIC_SPEED_CHECK,
    bootstrap_servers=KAFKA_BROKER_URL,
    value_deserializer=lambda value: json.loads(value),
)

async def time(websocket, path):
    while True:
        for message in consumer:
            result: dict = message.value
            print(TOPIC_SPEED_CHECK, result, flush=True)
            await websocket.send('{}'.format(result))

async def main():
    async with websockets.serve(time, Host, 8005):
        await asyncio.Future()  # run forever

asyncio.run(main())