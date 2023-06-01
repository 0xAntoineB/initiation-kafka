# Initiation-Kafka

### ``` git clone git@github.com:0xToonsy/initiation-kafka.git ```

Mettre les fichiers python et docker dans un seul et même dossier 

``` docker compose up -d ```

Si les containers python ne work pas, lancer les scripts directement sur l'host en ouvrant deux terminal, activer l'environnement python et installer la librairie de kafka.

```python -m venv env
    . env/bin/active
    pip install kafka-python
 ```
    
Lancer le script consumer.py

```python3 consumer.py```

Puis lancer le script producer.py

```python3 producer.py```
