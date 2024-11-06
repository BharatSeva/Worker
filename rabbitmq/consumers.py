import json
import databases.mongo as mn
import sendemail.mail as mail


def patient_records(ch, method, properties, body):
    try:
        data = json.loads(body)
        mn.insert_mongodb(data["record"], "patient_records")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Message Processing Error: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag)

def consume_logs(ch, method, properties, body):
    try:
        data = json.loads(body)
        category = data['category']
        mn.insert_mongodb(data, category, "logs")
        # send mail 
        #mail.send_mail(data)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Message Processing Error: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag)



def consume_appointments(ch, method, properties, body):
    try:
        data = json.loads(body)
        mn.insert_mongodb(data, "appointments", "db")
        # send mail
        #mail.send_mail(data)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Message Processing Error: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag)

def appointment_update(ch, method, properties, body):
    try:
        data = json.loads(body)

        # category = data['category'].split(':')[1]
        mn.insert_mongodb(data["appointments"], "appointment_update", "logs")

        # send mail
        #mail.send_mail(data)

        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Message Processing Error: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag)
