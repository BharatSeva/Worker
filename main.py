import rabbitmq.connection as conn
from dotenv import load_dotenv
import os
load_dotenv()

RABBITMQ_HOST=os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT=os.getenv("RABBITMQ_PORT")
RABBITMQ_USER=os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD=os.getenv("RABBITMQ_PASSWORD")

if __name__ == "__main__":
    rabbitmqconn = {
        "rabbitmq_host" : RABBITMQ_HOST,
        "rabbitmq_port" : RABBITMQ_PORT,
        "rabbitmq_user" : RABBITMQ_USER,
        "rabbitmq_password" : RABBITMQ_PASSWORD,
    }
    try:
        conn.start_consumer(rabbitmqconn)
        print("Consumer Service Started!!")
    except KeyboardInterrupt:
        print("Consumer stopped.")
