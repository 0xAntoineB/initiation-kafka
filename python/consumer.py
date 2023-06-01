from kafka import KafkaConsumer

bootstrap_servers = 'kafka:29092'
topic = 'my_topic'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group'
)

for message in consumer:
    print(f"Message reçu: {message.value.decode('utf-8')}")

consumer.close()

