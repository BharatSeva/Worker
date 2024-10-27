def send_patientId_created(user_name, health_id):
    subject = "Your Health ID Has Been Successfully Created"
    body = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                color: #333;
                background-color: #f9f9f9;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
            }}
            h2 {{
                color: #4CAF50;
            }}
            .footer {{
                font-size: 0.9em;
                color: #777;
                text-align: center;
                padding-top: 10px;
                border-top: 1px solid #e0e0e0;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Welcome, {user_name}!</h2>
            <p>We are excited to inform you that your Health ID has been successfully created.</p>
            <p><strong>Health ID:</strong> {health_id}</p>
            <p>This Health ID allows you secure access to manage your health records, appointments, and other services through our platform.</p>
            <p>If you have any questions, feel free to reach out to our support team.</p>
            <p>Thank you for choosing us to support your healthcare journey!</p>
            <p>Best Regards,<br>BharatSeva+ Healthcare Team</p>
            <div class="footer">
                <p>&copy; 2024 BharatSeva+ Healthcare Services. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """

    return {
        "subject": subject,
        "body": body,
    }

def send_medical_record_email(user_name, id):    
    Subject = "Your Medical Records Have Been Created"
    body = f"""
    <html>
    <body>
        <h2 style="color: #2e6c80;">Hello {user_name},</h2>
        <p><strong>Your HealthID:</strong> <span style="color: #2e6da4;">{id}</span></p>
        <p style="font-size: 16px;">We are pleased to inform you that your medical records have been successfully created and securely stored in our system.</p>

        <p style="font-size: 16px;">You can now access your records, book appointments, and receive timely notifications about your healthcare activities. 
        Our platform is designed to keep all your information confidential and easily accessible.</p>

        <p style="font-size: 16px;">If you have any questions or need further assistance, please don't hesitate to contact us.</p>

        <p style="font-size: 16px;">Warm regards,</p>
        <p style="font-weight: bold; font-size: 16px;">Your Healthcare Team</p>
    </body>
    </html>
    """

    return {
        "subject" : Subject,
        "body" : body,
    }

def send_welcome_healthcare_id(user_name, id):
    subject = "Welcome to BharatSeva+ Healthcare – Your Healthcare ID is Ready"
    
    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background-color: white; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); overflow: hidden;">
        
            <div style="background-color: #2e6da4; color: white; padding: 20px; text-align: center;">
                <h1>Welcome to BharatSeva+ Healthcare</h1>
            </div>
            
            <div style="padding: 20px;">
                <h2 style="color: #2e6da4;">Dear {user_name},</h2>
                <p style="font-size: 16px; line-height: 1.6;">
                    We are excited to welcome you to our healthcare community! Your healthcare ID has been successfully generated, and you're now ready to access all our services and benefits.
                </p>
                
                <p style="font-size: 16px; line-height: 1.6;"><strong>Your Healthcare ID:</strong> 
                    <span style="color: #2e6da4; font-size: 18px;">{id}</span>
                </p>
                
                <p style="font-size: 16px; line-height: 1.6;"><strong>Your Healthcare Name:</strong> 
                    <span style="color: #2e6da4; font-size: 18px;">{user_name}</span>
                </p>
                
                <p style="font-size: 16px; line-height: 1.6;">With this ID, you can now:</p>
                
                <ul style="font-size: 16px; line-height: 1.6;">
                    <li>Securely access and manage patient records</li>
                    <li>Schedule and review appointments</li>
                    <li>Receive health-related updates and notifications</li>
                </ul>

                <p style="font-size: 16px; line-height: 1.6;">
                    If you have any questions or need assistance, don't hesitate to reach out to our support team. We're here to help you make the most of our healthcare services.
                </p>
                
                <p style="font-size: 16px; line-height: 1.6;">Thank you for choosing BharatSeva+ Healthcare. We look forward to supporting you in providing exceptional care.</p>
                
                <p style="font-size: 16px; line-height: 1.6;">Warm regards,<br>
                <span style="color: #2e6da4; font-weight: bold;">The BharatSeva+ Healthcare System Team</span>
                </p>
            </div>
            
            <div style="background-color: #f8f8f8; padding: 15px; text-align: center; font-size: 12px; color: #999;">
                © {2024} BharatSeva+ Healthcare System. All rights reserved. | <a href="#" style="color: #2e6da4; text-decoration: none;">Contact Support</a>
            </div>
        </div>
    </body>
    </html>
    """
    
    return {
        "subject": subject,
        "body": body
    }

def send_loggedin(user_name, id):
    subject = "Login Activity Recorded – Healthcare ID Alert"
    
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                color: #333;
                background-color: #f8f8f8;
                margin: 0;
                padding: 0;
            }}
            .email-container {{
                max-width: 600px;
                margin: 30px auto;
                padding: 20px;
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                font-size: 26px;
                font-weight: bold;
                color: #2e6da4;
                padding-bottom: 20px;
                border-bottom: 1px solid #e6e6e6;
            }}
            .content {{
                margin-top: 20px;
                font-size: 16px;
                line-height: 1.8;
                color: #555;
            }}
            .highlight {{
                color: #2e6da4;
                font-weight: bold;
            }}
            .btn {{
                display: inline-block;
                padding: 10px 20px;
                margin-top: 30px;
                background-color: #2e6da4;
                color: #ffffff;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
                text-align: center;
            }}
            .footer {{
                margin-top: 30px;
                font-size: 14px;
                color: #999;
                text-align: center;
            }}
            .note {{
                font-size: 12px;
                color: #888;
                margin-top: 10px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">Login Activity Alert</div>
            
            <div class="content">
                <p>Dear <span class="highlight">{user_name}</span>,</p>

                <p>We have recorded a login activity for your healthcare account associated with the following details:</p>
                
                <p><strong>Healthcare ID:</strong> <span class="highlight">{id}</span></p>
                
                <p>If this login was made by you or an authorized individual, no action is required. However, if you suspect this activity to be unauthorized, we recommend that you secure your account immediately.</p>
                
                <p>If you have any concerns or questions, please contact our support team at <a href="mailto:support@healthcare.com">support@healthcare.com</a>.</p>

                <a href="https://your-support-link.com" class="btn">Secure Your Account</a>
            </div>

            <div class="footer">
                Warm regards,<br>
                The Bharat Seva+ Healthcare Team
            </div>
            
            <div class="note">
                This is an automated message – please do not reply directly to this email.
            </div>
        </div>
    </body>
    </html>
    """
    
    return {
        "subject": subject,
        "body": body
    }

def send_biodata_viewed(user_name, healthcare_name):
    subject = "Your Biodata Has Been Viewed by a Healthcare Provider"
    
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                color: #333;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .email-container {{
                max-width: 600px;
                margin: 30px auto;
                padding: 20px;
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                font-size: 26px;
                font-weight: bold;
                color: #2e6da4;
                padding-bottom: 20px;
                border-bottom: 1px solid #e6e6e6;
            }}
            .content {{
                margin-top: 20px;
                font-size: 16px;
                line-height: 1.8;
                color: #555;
            }}
            .highlight {{
                color: #2e6da4;
                font-weight: bold;
            }}
            .btn {{
                display: inline-block;
                padding: 10px 20px;
                margin-top: 30px;
                background-color: #2e6da4;
                color: #ffffff;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
                text-align: center;
            }}
            .footer {{
                margin-top: 30px;
                font-size: 14px;
                color: #999;
                text-align: center;
            }}
            .note {{
                font-size: 12px;
                color: #888;
                margin-top: 10px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">Biodata Viewed Notification</div>
            
            <div class="content">
                <p>Dear <span class="highlight">{user_name}</span>,</p>

                <p>We wanted to inform you that your biodata has been recently viewed by a healthcare provider:</p>
                
                <p><strong>Healthcare Provider:</strong> <span class="highlight">{healthcare_name}</span></p>
                
                <p>This activity is a routine part of our services when healthcare providers access records to provide better care and ensure accurate health data management. If you have any concerns or questions about this activity, feel free to reach out to us.</p>
                
                <p>For any assistance, you can contact our support team at <a href="mailto:support@healthcare.com">support@healthcare.com</a>.</p>

                <a href="https://your-healthcare-dashboard.com" class="btn">View Your Activity</a>
            </div>

            <div class="footer">
                Best regards,<br>
                The Bharat Seva+ Healthcare Team
            </div>
            
            <div class="note">
                Note: This is an automated message – please do not reply directly to this email.
            </div>
        </div>
    </body>
    </html>
    """
    
    return {
        "subject": subject,
        "body": body
    }

def send_records_viewed(user_name, healthcare_name):
    subject = "Your Medical Records Have Been Viewed by a Healthcare Provider"
    
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                color: #333;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .email-container {{
                max-width: 600px;
                margin: 30px auto;
                padding: 20px;
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                font-size: 26px;
                font-weight: bold;
                color: #2e6da4;
                padding-bottom: 20px;
                border-bottom: 1px solid #e6e6e6;
            }}
            .content {{
                margin-top: 20px;
                font-size: 16px;
                line-height: 1.8;
                color: #555;
            }}
            .highlight {{
                color: #2e6da4;
                font-weight: bold;
            }}
            .btn {{
                display: inline-block;
                padding: 10px 20px;
                margin-top: 30px;
                background-color: #2e6da4;
                color: #ffffff;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
                text-align: center;
            }}
            .footer {{
                margin-top: 30px;
                font-size: 14px;
                color: #999;
                text-align: center;
            }}
            .note {{
                font-size: 12px;
                color: #888;
                margin-top: 10px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">Medical Records Accessed Notification</div>
            
            <div class="content">
                <p>Dear <span class="highlight">{user_name}</span>,</p>

                <p>We would like to inform you that your medical records have been viewed by a healthcare provider:</p>
                
                <p><strong>Healthcare Provider:</strong> <span class="highlight">{healthcare_name}</span></p>
                
                <p>This activity is part of the standard healthcare process and is done to ensure that your medical history is properly managed for better care. If you have any concerns about this access or feel it wasn’t authorized, we encourage you to reach out to our support team immediately.</p>
                
                <p>If you have any questions or need assistance, feel free to contact us at <a href="mailto:support@healthcare.com">support@healthcare.com</a>.</p>

                <a href="https://your-healthcare-dashboard.com" class="btn">View Your Record Activity</a>
            </div>

            <div class="footer">
                Best regards,<br>
                The Bharat Seva+ Healthcare Team
            </div>
            
            <div class="note">
                This is an automated message – please do not reply directly to this email.
            </div>
        </div>
    </body>
    </html>
    """
    
    return {
        "subject": subject,
        "body": body
    }

def send_biodata_updated(user_name, healthcare_name):
    subject = "Your Biodata Has Been Successfully Updated"
    
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                color: #333;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .email-container {{
                max-width: 600px;
                margin: 30px auto;
                padding: 20px;
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                font-size: 26px;
                font-weight: bold;
                color: #2e6da4;
                padding-bottom: 20px;
                border-bottom: 1px solid #e6e6e6;
            }}
            .content {{
                margin-top: 20px;
                font-size: 16px;
                line-height: 1.8;
                color: #555;
            }}
            .highlight {{
                color: #2e6da4;
                font-weight: bold;
            }}
            .btn {{
                display: inline-block;
                padding: 10px 20px;
                margin-top: 30px;
                background-color: #2e6da4;
                color: #ffffff;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
                text-align: center;
            }}
            .footer {{
                margin-top: 30px;
                font-size: 14px;
                color: #999;
                text-align: center;
            }}
            .note {{
                font-size: 12px;
                color: #888;
                margin-top: 10px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">Biodata Update Notification</div>
            
            <div class="content">
                <p>Dear <span class="highlight">{user_name}</span>,</p>

                <p>We would like to inform you that your biodata has been successfully updated by the following healthcare provider:</p>
                
                <p><strong>Healthcare Provider:</strong> <span class="highlight">{healthcare_name}</span></p>
                
                <p>This update is part of our commitment to ensure your health records are accurate and current. If you have any questions regarding this update or if you believe any information is incorrect, please do not hesitate to reach out to us.</p>
                
                <p>For any assistance, you can contact our support team at <a href="mailto:support@healthcare.com">support@healthcare.com</a>.</p>

                <a href="https://your-healthcare-dashboard.com" class="btn">View Your Updated Biodata</a>
            </div>

            <div class="footer">
                Best regards,<br>
                The Bharat Seva+ Healthcare Team
            </div>
            
            <div class="note">
                This is an automated message – please do not reply directly to this email.
            </div>
        </div>
    </body>
    </html>
    """
    
    return {
        "subject": subject,
        "body": body
    }

def send_appointment_scheduled(user_name, healthcare_name, appointment_date, appointment_time):
    subject = "Your Appointment Has Been Successfully Scheduled"
    
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                color: #333;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .email-container {{
                max-width: 600px;
                margin: 30px auto;
                padding: 20px;
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                font-size: 26px;
                font-weight: bold;
                color: #2e6da4;
                padding-bottom: 20px;
                border-bottom: 1px solid #e6e6e6;
            }}
            .content {{
                margin-top: 20px;
                font-size: 16px;
                line-height: 1.8;
                color: #555;
            }}
            .highlight {{
                color: #2e6da4;
                font-weight: bold;
            }}
            .btn {{
                display: inline-block;
                padding: 10px 20px;
                margin-top: 30px;
                background-color: #2e6da4;
                color: #ffffff;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
                text-align: center;
            }}
            .footer {{
                margin-top: 30px;
                font-size: 14px;
                color: #999;
                text-align: center;
            }}
            .note {{
                font-size: 12px;
                color: #888;
                margin-top: 10px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">Appointment Confirmation</div>
            
            <div class="content">
                <p>Dear <span class="highlight">{user_name}</span>,</p>

                <p>We are pleased to inform you that your appointment has been successfully scheduled with:</p>
                
                <p><strong>Healthcare Provider:</strong> <span class="highlight">{healthcare_name}</span></p>
                <p><strong>Appointment Date:</strong> <span class="highlight">{appointment_date}</span></p>
                <p><strong>Appointment Time:</strong> <span class="highlight">{appointment_time}</span></p>
                
                <p>Please make sure to arrive a few minutes early and bring any necessary documents. If you need to reschedule or have any questions regarding your appointment, feel free to contact our support team.</p>
                
                <p>If you require further assistance, reach out to us at <a href="mailto:support@healthcare.com">support@healthcare.com</a>.</p>

                <a href="https://your-healthcare-dashboard.com" class="btn">View Your Appointment Details</a>
            </div>

            <div class="footer">
                Best regards,<br>
                The Bharat Seva+ Healthcare Team
            </div>
            
            <div class="note">
                This is an automated message – please do not reply directly to this email.
            </div>
        </div>
    </body>
    </html>
    """
    
    return {
        "subject": subject,
        "body": body
    }

def send_hip_deletion_scheduled(user_name, id):
    subject = "Important Notice: Healthcare ID Deletion Scheduled"
    body = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Healthcare ID Deletion Notice</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    color: #333333;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #ffffff;
                    padding: 20px;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                }}
                .header {{
                    text-align: center;
                    background-color: #4CAF50;
                    padding: 10px;
                    color: #ffffff;
                    border-radius: 8px 8px 0 0;
                }}
                .content {{
                    padding: 20px;
                    font-size: 16px;
                    line-height: 1.6;
                }}
                .cta {{
                    background-color: #e74c3c;
                    color: #ffffff;
                    text-align: center;
                    padding: 12px;
                    border-radius: 5px;
                    font-size: 18px;
                    text-decoration: none;
                    display: inline-block;
                    margin-top: 20px;
                }}
                .footer {{
                    text-align: center;
                    font-size: 14px;
                    color: #777777;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>

        <div class="container">
            <div class="header">
                <h2>Important Notice: Healthcare ID Deletion Scheduled</h2>
            </div>
            <div class="content">
                <p>Dear {user_name},</p>
                <p>We are reaching out to inform you that your Healthcare ID <strong>{id}</strong> has been scheduled for deletion as per our policy. If you would like to retain your account, please contact us as soon as possible.</p>

                <p><strong>Scheduled Deletion Date:</strong> Within 2 months from the date of this email</p>
                
                <p>If this deletion was not intended, please contact us immediately at <a href="mailto:21vaibhav11@gmail.com">21vaibhav11@gmail.com</a> to prevent your Healthcare ID from being permanently deleted.</p>

                <p>Once deleted, all data associated with your ID will be permanently removed from our systems and cannot be restored.</p>

                <a href="mailto:21vaibhav11@gmail.com" class="cta">Contact Support</a>
            </div>
            <div class="footer">
                <p>Thank you for trusting us with your healthcare information.</p>
                <p>Best regards, <br> [Your Organization's Name]</p>
            </div>
        </div>

        </body>
        </html>
    """
    return {
        "subject":subject,
        "body":body
    }





