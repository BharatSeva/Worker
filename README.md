
# Worker Service  [![Deploy to AzureVM](https://github.com/BharatSeva/Worker/actions/workflows/deploy.yaml/badge.svg)](https://github.com/BharatSeva/Worker/actions/workflows/deploy.yaml)  
A robust **Python-based Worker Service** designed for the **Bharat Seva+** backend system. This service leverages message-driven architecture to handle events and data processing efficiently. It continuously listens to RabbitMQ queues, processes logs, appointments, and medical records, and manages email notifications. Processed data is stored in PostgreSQL and MongoDB, enabling structured and unstructured data handling for reliable service delivery.

---

## Features

- **Asynchronous Processing**: Consumes and processes messages from RabbitMQ, allowing non-blocking tasks.
- **Database Integration**:
  - **PostgreSQL**: Stores structured, relational data, ideal for transactions and structured healthcare records.
  - **MongoDB**: Stores document-based data, suitable for unstructured and flexible data requirements.
- **Email Notifications**: Sends timely notifications for appointments and other healthcare updates to patients and staff.
- **Reliable Message Queueing**: Efficient message handling using RabbitMQ for logging, appointments, medical records, and updates.
  
---

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Docker Setup](#docker-setup)
- [License](#license)

---

## Requirements

- **Python** 3.8+
- **RabbitMQ** (with appropriate queues configured)
- **PostgreSQL** and **MongoDB** databases

### Python Packages:
- `pika` (for RabbitMQ integration)
- `psycopg2` (for PostgreSQL interaction)
- `pymongo` (for MongoDB interaction)
- `smtplib` (for email handling)

---

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/BharatSeva/Worker.git
    cd Worker
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## Configuration

### Environment Variables

Configure environment variables for secure access to services. You can set these in a `.env` file or export them in the shell. Below are the required environment variables:

```plaintext
# RabbitMQ
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_USER=rootuser
RABBITMQ_PASSWORD=rootuser

# MongoDB
MONGODB_URL=mongodb://rootuser:rootuser@mongodb:27017?authSource=admin
MONGODB_USER=rootuser
MONGODB_PASSWORD=rootuser

# PostgreSQL
POSTGRESQL_URL=postgres://rootuser:rootuser@postgres:5432/postgres?sslmode=disable
POSTGRESQL_USER=rootuser
POSTGRESQL_PASSWORD=rootuser
POSTGRESQL_PORT=5432
POSTGRESQL_HOST=postgres
POSTGRESQL_DB=postgres

# SMTP for Email Notifications
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
SMTP_EMAIL=<your-email>
SMTP_PASSWORD=<your-one-time-password>
```
### Setting Up RabbitMQ Queues
Ensure that the following RabbitMQ queues are available:
- logs
- patient_records
- appointments_queue
- appointment_update

## Usage
The service continuously listens to the specified RabbitMQ queues and processes messages accordingly.

Run the Consumer Service:

```bash
python main.py
```
Run Using Docker: Build and run the service within a Docker container if Docker is part of your deployment setup. This service is configured for containerized environments.

### Docker Setup
Build the Docker Image:

```bash
docker build -t worker .
```
Run the Docker Container:

```bash
docker run -d --env-file .env worker
```
## License
This project is licensed under the AGPL-3.0 License. See the [LICENSE](./LICENSE) file for more details.
