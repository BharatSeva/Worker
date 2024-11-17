import json
import databases.mongo as mn
import sendemail.mail as mail
from databases.postgres import counter_update_client_postgresql, counter_update_healthcare_postgresql, Insert_appointment_section
import databases.postgres as pg

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

        # Update posgreSQL counters
        valid_counters = ["profile_viewed", "profile_updated", "records_viewed", "records_created"]
        if data['category'] in valid_counters:
            # update client postgres
            counter_update_client_postgresql(data['category'], data['health_id'])
            # update healthcareuser postgres
            counter_update_healthcare_postgresql(data['category'], data['healthcare_id'])

        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Message Processing Error: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag)

def consume_appointments(ch, method, properties, body):
    try:
        data = json.loads(body)
        # mn.insert_mongodb(data, "appointments", "db")
        Insert_appointment_section(data)
        # send mail
        #mail.send_mail(data)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Message Processing Error: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag)

def appointment_update(ch, method, properties, body):
    try:
        data = json.loads(body)
        pg.Update_appointment_status(data["update"])

        # send mail
        #mail.send_mail(data)
        
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Message Processing Error: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag)








