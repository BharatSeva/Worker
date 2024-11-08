import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

POSTGRESQL_PORT=os.getenv("POSTGRESQL_PORT")
POSTGRESQL_PASSWORD=os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_USER=os.getenv("POSTGRESQL_USER")
POSTGRESQL_URL=os.getenv("POSTGRESQL_URL")
POSTGRESQL_HOST=os.getenv("POSTGRESQL_HOST")
POSTGRESQL_DB=os.getenv("POSTGRESQL_DB")

pg_connection = psycopg2.connect(
    dbname=POSTGRESQL_DB,
    user=POSTGRESQL_USER,
    password=POSTGRESQL_PASSWORD,
    host=POSTGRESQL_HOST
)

pg_cursor = pg_connection.cursor()
def insert_postgresql(data):
    try:
        query = "INSERT INTO hip_table (name, id) VALUES (%s, %s);"
        pg_cursor.execute(query, (data['field1'], data['field2']))
        pg_connection.commit()
    except Exception as e:
        print(f"PostgreSQL Error: {e}")
        pg_connection.rollback()



pg_cursor.close()
pg_connection.close()
        