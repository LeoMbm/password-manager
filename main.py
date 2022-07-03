# Firstly, I imported the module for psycopg
import dotenv
import psycopg2
import os
dotenv.load_dotenv()
# I connect my db and I print that if connected
conn = psycopg2.connect(database=os.getenv("database"),
                        user=os.getenv("user"),
                        password=os.getenv("password"),
                        host=os.getenv("host"),
                        port=os.getenv("port"))

print("Connection Successful to PostgresSQL")

cur = conn.cursor()
# query = "DELETE FROM password;"
# cur.execute(query)
cur.execute("select * from password;")
rows = cur.fetchall()

for r in rows:
    print(r[0], r[1], r[2], r[3])
conn.commit()
cur.close()
conn.close()
