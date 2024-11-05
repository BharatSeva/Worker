import pika
from .consumers import (consume_logs, consume_patient_records, 
                        consume_appointments, consume_patient_logs)


def start_consumer(rabbitmqconn):
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

    # listen for hip:logs, first create queue and listen to it
    channel.queue_declare(queue="hip:logs", durable=False)
    channel.basic_consume(queue="hip:logs", on_message_callback=consume_logs)
    
    # listen for patient_records created
    channel.queue_declare(queue="hip:patient_records", durable=False)
    channel.basic_consume(queue="hip:patient_records", on_message_callback=consume_patient_records)


    channel.queue_declare(queue="appointments_queue", durable=True)
    channel.basic_consume(queue="appointments_queue", on_message_callback=consume_appointments)

    # for patient logs
    channel.queue_declare(queue="patient_logs", durable=True)
    channel.basic_consume(queue="patient_logs", on_message_callback=consume_patient_logs)

    print("[*] Waiting for messages. To exit, press CTRL+C")
    channel.start_consuming()



