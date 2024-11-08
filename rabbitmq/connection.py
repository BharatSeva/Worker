import pika
import time
from .consumers import (consume_logs, patient_records, 
                        consume_appointments,
                        appointment_update)


def start_consumer(rabbitmqconn):
    while True:
        try:
            print("[*] Attempting to connect to RabbitMQ...")
            
            credentials = pika.PlainCredentials(rabbitmqconn["rabbitmq_user"], rabbitmqconn["rabbitmq_password"])
            parameters = pika.ConnectionParameters(
                host=rabbitmqconn["rabbitmq_host"],
                port=rabbitmqconn["rabbitmq_port"], 
                virtual_host='/',
                credentials=credentials,
                heartbeat=300
            )

            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            channel.basic_qos(prefetch_count=1)

            print("[*] Connected to RabbitMQ. Declaring queues and starting consumers...")

            channel.queue_declare(queue="logs", durable=False)
            print("[*] Listening on 'logs' queue...")
            channel.basic_consume(queue="logs", on_message_callback=consume_logs)
            
            channel.queue_declare(queue="patient_records", durable=False)
            print("[*] Listening on 'patient_records' queue...")
            channel.basic_consume(queue="patient_records", on_message_callback=patient_records)
            
            channel.queue_declare(queue="appointments_queue", durable=True)
            print("[*] Listening on 'appointments_queue' queue...")
            channel.basic_consume(queue="appointments_queue", on_message_callback=consume_appointments)
            
            channel.queue_declare(queue="appointment_update", durable=False)
            print("[*] Listening on 'appointment_update' queue...")
            channel.basic_consume(queue="appointment_update", on_message_callback=appointment_update)

            print("[*] Waiting for messages. To exit, press CTRL+C")
            channel.start_consuming()

        except pika.exceptions.AMQPConnectionError as e:
            print(f"[!] Connection error: {e}. Retrying in 5 seconds...")
            time.sleep(5)
        except Exception as e:
            print(f"[!] Unexpected error: {e}. Exiting consumer loop.")
            break

