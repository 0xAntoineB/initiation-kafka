from kafka import KafkaProducer

bootstrap_servers = 'kafka:29092'
topic = 'my_topic'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

messages = ['Message 1', 'Message 2', 'Message 3']

for message in messages:

    try:

        producer.send(topic, value=message.encode('utf-8'))
        print(f"Message envoyé : {message}")

    except Exception as e:

        print(f"Erreur lors de l'envoi du message : {message}")
        print(str(e))

producer.flush()
producer.close()

