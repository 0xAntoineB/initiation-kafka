from kafka import KafkaConsumer
import mysql.connector



db = connect_db() 
cursor = db.cursor()

consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=kafka_bootstrap_servers,
    group_id='group',
    auto_offset_reset='earliest'  
)

for message in consumer:

    if message.value:

        csv_row = message.value.decode('utf-8')

        row_data = csv_row.split(',')

        nom = row_data[0]
        prenom = row_data[1]
        numero = row_data[2]

        query = f"SELECT COUNT(*) FROM {mysql_table} WHERE nom = %s AND prenom = %s AND numero = %s"
        values = (nom, prenom, numero)
        cursor.execute(query, values)
        count = cursor.fetchone()[0]

        if count == 0:

            query = f"INSERT INTO {mysql_table} (nom, prenom, numero) VALUES (%s, %s, %s)"
            cursor.execute(query, values)
            db.commit()

            print("Données insérées en base de données :", row_data)

        else:

            print("Enregistrement déjà existant :", row_data)

consumer.close()
cursor.close()
db.close()
