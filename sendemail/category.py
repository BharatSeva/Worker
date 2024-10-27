
from .template import (send_loggedin, send_patientId_created, 
                       send_welcome_healthcare_id, send_medical_record_email,
                       send_biodata_viewed, send_records_viewed,
                       send_biodata_updated, send_appointment_scheduled,
                       send_hip_deletion_scheduled                  
                       )


def select_message(data):
    category = data['category'].split(":")[1]
    # user_name = data.get('hip_name') or data.get('patient_name')
    # if not user_name:
    #     user_name = "user"

    # user_id = data.get('healthcareId') or data.get('healthId')
    # if not user_id:
    #     user_id  = "user"
    

    # patient bio data has been created
    if category == "patient_biodata_created":
        user_name = data.get('patient_name')
        user_id = data.get('healthId')
        return send_patientId_created(user_name, user_id)

        # healthcare accoutn created 
    elif category == "account_created":
        user_name = data.get('hip_name')
        user_id = data.get('healthcareId')
        return send_welcome_healthcare_id(user_name, user_id)

        # healthcare account login
    elif category == "account_login":
        user_name = data.get('hip_name')
        user_id = data.get('healthcareId')
        return send_loggedin(user_name, user_id)

        # patient record has been created
    elif category == "patient_record_created":
        user_name = data.get('patient_name') or "User"
        user_id = data.get('healthId')
        return send_medical_record_email(user_name, user_id)

        # patient bio data has been viewed
    elif category == "patient_biodata_viewed":
        user_name = data.get('patient_name') or "User"
        healthcare_name = data.get('healthcare_name')
        return send_biodata_viewed(user_name, healthcare_name)
    
        # patient records has been viewed 
    elif category == "patient_record_viewed":
        user_name = data.get('patient_name') or "User"
        healthcare_name = data.get('healthcare_name') or "Registered Healthcare HIU"
        return send_records_viewed(user_name, healthcare_name)

        # patient bio data has been updated
    elif category == "patient_biodata_updated":
        user_name = data.get('patient_name') or "User"
        healthcare_name = data.get('healthcare_name') or "Registered Healthcare HIU"
        return send_biodata_updated(user_name, healthcare_name)

        # user healthcare id has been schduled for deletion
    elif category == "delete_account":
        user_name = data.get('hip_name')
        user_id = data.get('healthcareId')
        return send_hip_deletion_scheduled(user_name, user_id)
    
    # return empty message
    return {}