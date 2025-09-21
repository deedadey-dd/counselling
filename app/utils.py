import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
# Connect to the database

print(os.getenv("DB_PASSWORD"))

try:
    connection = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"), 
        password = os.getenv("DB_PASSWORD"),
        port = os.getenv("DB_PORT"),
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Sample Query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"connection successful | db version: {db_version[0]}")

    
except psycopg2.Error as e:
    cursor = None
    print(f'Error connecting to database: {e}')

finally:
    if cursor:
        cursor.close()
    # if connection: 
    #     connection.close()
    print('Connection Closed')
