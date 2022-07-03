import psycopg2
import os


# I connect my db and I print that if connected
def dbconfig():
    connection = psycopg2.connect(database=os.getenv("database"),
                                  user=os.getenv("user"),
                                  password=os.getenv("password"),
                                  host=os.getenv("host"),
                                  port=os.getenv("port"))
    print("Connection Successful to PostgresSQL")
    return connection
