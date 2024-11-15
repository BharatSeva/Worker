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
    host=POSTGRESQL_HOST,
    port=POSTGRESQL_PORT,
)

pg_cursor = pg_connection.cursor()
def counter_update_client_postgresql(category, health_id):
    try:        
        query = f"UPDATE client_stats SET {category} = {category} + 1 WHERE health_id = %s;"
        pg_cursor.execute(query, (health_id,))
        pg_connection.commit()
        print(f"{category} counter updated successfully for health_id {health_id}.")
    except Exception as e:
        print(f"PostgreSQL Error: {e}")
        pg_connection.rollback()

def counter_update_healthcare_postgresql(category, healthcare_id):
    try:        
        query = f"UPDATE healthcare_pref SET {category} = {category} + 1 WHERE healthcare_id = %s;"
        pg_cursor.execute(query, (healthcare_id,))
        pg_connection.commit()
        print(f"{category} counter updated successfully for healthcare_id {healthcare_id}.")
    except Exception as e:
        print(f"PostgreSQL Error: {e}")
        pg_connection.rollback()


# pg_cursor.close()
# pg_connection.close()
