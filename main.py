import rabbitmq.connection as conn
from dotenv import load_dotenv
import os


if __name__ == "__main__":
    rabbitmqconn = {
        "rabbitmq_host" : 'localhost',
        "rabbitmq_port" : 5672,
        "rabbitmq_user" : 'rootuser',
        "rabbitmq_password" : 'rootuser',
    }
    try:
        conn.start_consumer(rabbitmqconn)
    except KeyboardInterrupt:
        print("Consumer stopped.")
