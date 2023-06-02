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


## Kafka avec SQL 

Avec les trois scripts python et une base de données, envoyé des données dans le producer de puis un fichier csv, puis insertion en base ave traitement de si la donnée n'existe déjà ou pas. 

Requirement pour les scripts : 

    - os
    - mysql-connector
    - Faker
    - csv
    - kafka

Ne pas oublier de lancer le docker compose avec kafka et de saisir les connexions dans les scritps 
Ne pas oublier la connexion MySQL dans le consumer avec la précision sur la base
Ne pas oublier de renseigner les chemins du csv que ça soit dans le script de génération puis dans le producer 
Avoir deux terminal d'ouvert

### Step 1 : Génération de donnée avec le scrip csvkafka.py

``` 
python3 csvkafka.py
```

### Step 2 : Lancement du fichier consumer pour voir apparaitre les données traitées.
```
python3 consumersqlcsv.py
```

### Step 3 : Lancement du fichier producer pour envoyé les données à Kafka 
```
python3 producersqlcsv.py
```

Les données iront directement en base de données.


Il est possible dans le terminal du producer de re générée d'autre donnée, réexecuter le producer autant de fois de donner régénérées.
Les données existantes ne seront pas insérées grâce au traitement, le terminal du consumer le précise.

