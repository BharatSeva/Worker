import psycopg2
pg_connection = psycopg2.connect(
    # dbname='your_dbname',
    user='rootuser',
    password='rootuser',
    host='postgres://rootuser:rootuser@localhost:5432/postgres?sslmode=disable'
)
pg_cursor = pg_connection.cursor()

def insert_postgresql(data):
    try:
        query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s);"
        pg_cursor.execute(query, (data['field1'], data['field2']))
        pg_connection.commit()
    except Exception as e:
        print(f"PostgreSQL Error: {e}")
        pg_connection.rollback()



pg_cursor.close()
pg_connection.close()
        