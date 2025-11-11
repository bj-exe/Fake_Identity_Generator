import mysql.connector
from faker import Faker

fake = Faker()

num_users = int(input("How many 5fake users do you want to create? "))

conn = mysql.connector.connect(
    host="localhost",       
    user="root",    
    password="",
    database="fakeridentity_db"       
)

cursor = conn.cursor()

query = """
INSERT INTO users (name, address, email, phone, company, job)
VALUES (%s, %s, %s, %s, %s, %s)
"""

values_list = []
for _ in range(num_users):
    name = fake.name()
    address = fake.address()
    email = fake.unique.email() 
    phone = fake.phone_number()
    company = fake.company()
    job = fake.job()

    values_list.append((name, address, email, phone, company, job))


cursor.executemany(query, values_list)
conn.commit()

print(f"{num_users} fake users inserted into database.")

cursor.close()
conn.close()
