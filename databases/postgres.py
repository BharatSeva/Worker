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

# Insert into appointment
def Insert_appointment_section(data):
    try:
        query = """
            INSERT INTO appointments (status, appointment_time, department, fullname, health_id, appointment_date, healthcare_id, note, healthcare_name, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        values = (
            data["status"],
            data["appointment_time"],
            data["department"],
            data["fullname"],
            data["health_id"],
            data["appointment_date"],
            data["healthcare_id"],
            data["note"],
            data["healthcare_name"],
            data["created_at"],
            data["updated_at"]
        )
        pg_cursor.execute(query, values)
        pg_connection.commit()
    except Exception as e:
        print(f"PostgreSQL Error: {e}")
        pg_connection.rollback()

# Update the status of appointments...
def Update_appointment_status(data):
    try:
        query = """
            UPDATE appointments
            SET status = %(status)s
            WHERE id = %(id)s 
            AND health_id = %(health_id)s 
            AND healthcare_id = %(healthcare_id)s;
        """
        values = {
            "status": data["status"],
            "id": data["id"],
            "health_id": data["health_id"],
            "healthcare_id": data["healthcare_id"]
        }
        pg_cursor.execute(query, values)
        pg_connection.commit()
    except Exception as e:
        print(f"PostgreSQL Error: {e}")
        pg_connection.rollback()

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
