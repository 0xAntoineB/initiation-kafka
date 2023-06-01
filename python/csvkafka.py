import csv
from faker import Faker

faker_locale = 'fr_FR'  
faker_seed = 1234  

csvfile = ''
csv_header = ['nom', 'prenom', 'numero']
csv_rows = 10  

faker = Faker(faker_locale)
Faker.seed(faker_seed)

with open(csvfile, 'a', newline='') as file:

    writer = csv.writer(file)
    writer.writerow(csv_header)

    for element in range(csv_rows):

        nom = faker.last_name()
        prenom = faker.first_name()
        numero = faker.phone_number()

        row = [nom, prenom, numero]
        writer.writerow(row)

print(f'Des données dans le fichier "{csvfile}" ont été rajouter.')

