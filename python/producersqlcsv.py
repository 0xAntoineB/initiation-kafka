from kafka import KafkaProducer
import csv

kafka_bootstrap_servers = '172.20.0.3:29092'
kafka_topic = 'topic'

csvfile = ''

producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers)

with open(csvfile, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  

    for row in csv_reader:
        nom = row[0]
        prenom = row[1]
        numero = row[2]

        csv_row = ','.join(row)

        producer.send(kafka_topic, value=csv_row.encode('utf-8'))

producer.close()

