# producer.py

import time
from time import sleep
from json import dumps
#from kafka import SimpleProducer, KafkaClient
from kafka import KafkaConsumer, KafkaProducer
#  connect to Kafka
producer = KafkaProducer(bootstrap_servers=['172.16.0.248:9092'], api_version=(0, 10), value_serializer=lambda x: dumps(x).encode('utf-8'))
# Assign a topic
topic = 'test01'
for e in range(10000):
    producer.send(topic, value=f'test : {e}')
    print('senttttt')
producer.flush()