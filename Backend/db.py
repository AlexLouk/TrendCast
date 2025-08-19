import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")

def get_connection():
    return(
        psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
        )
    )

def check_user(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT {email} FROM users")

def create_users_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (" \
    "id SERIAL PRIMARY KEY," \
    "email VARCHAR(255) UNIQUE NOT NULL," \
    "password_hash VARCHAR(255) NOT NULL," \
    "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
    )
    conn.commit()
    cursor.close()
    conn.close()


# Example query
#cursor.execute("SELECT NOW();")
#result = cursor.fetchone()
#print("Current Time:", result)

# Close the cursor and connection
#cursor.close()
#connection.close()
#print("Connection closed.")