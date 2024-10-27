# Healthcare Consumer Service

A Python-based consumer service designed for the **Bharat Seva+** healthcare backend. This service listens to RabbitMQ queues, processes logs, appointments, medical records, and handles email notifications. Data is inserted into PostgreSQL and MongoDB databases.

---

## Features
- **Message Queue**: Consumes messages from RabbitMQ queues for:
  - Logs
  - Appointments
  - Medical Records
- **Database Integration**:
  - **PostgreSQL**: Stores relational data.
  - **MongoDB**: Stores document-based data for unstructured records.
- **Email Notifications**: Sends notifications for appointments and other healthcare updates.

---

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

---

## Requirements
- **Python** 3.8+
- **RabbitMQ** (with appropriate queues set up)
- **PostgreSQL** and **MongoDB** databases

Python Packages:
- `pika` (for RabbitMQ integration)
- `psycopg2` (for PostgreSQL)
- `pymongo` (for MongoDB)
- `smtplib` (for email handling)

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd healthcare-consumer-service
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
### Environment Variables
Set up environment variables for secure configurations. Use `.env` file or export in shell:

```plaintext
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_USER=rootuser
RABBITMQ_PASSWORD=rootuser

POSTGRESQL_URI=postgres://rootuser:rootuser@localhost:5432/postgres?sslmode=disable
POSTGRESQL_USER=rootuser
POSTGRESQL_PASSWORD=rootuser

MONGODB_URI=mongodb://rootuser:rootuser@localhost:27017
MONGODB_USER=rootuser
MONGODB_PASSWORD=rootuser

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=465
EMAIL_USER=<your-email>
EMAIL_PASSWORD=<your-one-time-password>
```

## Usage
The service will continuously listen to the specified RabbitMQ queues and process messages accordingly.

Run the consumer service:
```bash
python main.py
```


## License
This project is licensed under the AGPL-3.0 license License. See the [LICENSE](./LICENSE) file for details.
