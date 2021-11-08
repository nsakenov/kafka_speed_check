import os
import json
from kafka import KafkaConsumer
import time
import firebase_admin
import threading
from firebase_admin import firestore
import asyncio


TOPIC_SPEED_CHECK = os.environ.get('TOPIC_SPEED_CHECK')
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')

consumer = KafkaConsumer(
    TOPIC_SPEED_CHECK,
    bootstrap_servers=KAFKA_BROKER_URL,
    value_deserializer=lambda value: json.loads(value),
)

# init Firebase
cred_object = firebase_admin.credentials.Certificate("firebase-sdk.json")
firebase_admin.initialize_app(cred_object)
firestore_db = firebase_admin.firestore.client()

#create & update
doc_ref = firestore_db.collection(u'speed').document('speed-checked') #.document(u'test')

for message in consumer:
    result: dict = message.value
    print(result, flush=True)
    doc_ref.set(result)
    