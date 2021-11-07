import json
import os
from kafka import KafkaConsumer, KafkaProducer
import time

time.sleep(50)

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TOPIC_CURRENT_SPEED = os.environ.get('TOPIC_CURRENT_SPEED')
TOPIC_SPEED_CHECK = os.environ.get('TOPIC_SPEED_CHECK')


def is_high(speed: dict) -> dict:
    """Determine whether speed exceeds the limit"""
    if speed['speed'] >= 100:
        speed['exceeds'] = True
    else: 
        speed['exceeds'] = False
    return speed
 

consumer = KafkaConsumer(
    TOPIC_CURRENT_SPEED,
    bootstrap_servers=KAFKA_BROKER_URL,
    value_deserializer=lambda value: json.loads(value),
)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER_URL,
    value_serializer=lambda value: json.dumps(value).encode(),
)
for message in consumer:
    speed: dict = message.value
    check_speed: dict = is_high(speed)
    print(TOPIC_SPEED_CHECK, check_speed, flush=True) #debugging
    producer.send(TOPIC_SPEED_CHECK, value=check_speed)

