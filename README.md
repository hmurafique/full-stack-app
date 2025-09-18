# Full-Stack-App

## 📌 Project Overview
**Full-Stack-App** is a microservices-based application designed to demonstrate a production-ready, modern architecture.
It integrates multiple backend services (authentication, payments, catalog, analytics, notifications, email, SMS, search), a dedicated API gateway, and a frontend service.
The system is containerized using Docker Compose, uses PostgreSQL and Redis as supporting services, and leverages RabbitMQ for messaging and Celery workers for background tasks.
Nginx is configured as a reverse proxy with SSL for secure communication and domain-based routing.

This project serves as a solid foundation for scalable, cloud-ready applications.

---

## Core Components
- **Frontend Service (React)**
- **Backend Service (Flask/Node)**
- **Auth Service (Flask)**
- **Payments Service (Node.js)**
- **Catalog Service (Flask)**
- **Analytics Service (Python)**
- **Notifications Service (Flask)**
- **Email Service (Flask)**
- **SMS Service (Flask)**
- **Search Service (Flask)**
- **Worker Service (Celery)**
- **Infrastructure**: PostgreSQL, Redis, RabbitMQ, Adminer
- **Nginx Service**: Nginx (host machine or containerized)

---

## 🚀 Prerequisites
Before running the project, ensure the following tools are installed on your host machine:
- **Docker** (>= 24.x)
- **Docker Compose** (>= 2.x)
- **Nginx** (for host machine reverse proxy, if not using containerized nginx)
- **Certbot** (for SSL certificates)
- A registered **Domain Name** with DNS A records pointing to your server’s public IP

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/full-stack-app.git
cd full-stack-app
```

---

### 2️⃣ Configure Environment Variables
- Create a **.env file** in the project root and define variables

---

### 3️⃣ Create the Dockerfiles
- Write **Dockerfiles** for each service (frontend, backend, auth, etc.) to containerize them.

---

### 4️⃣ Create the Docker Compose File
- Define all services in a **docker-compose.yml** file.

---

# Phase 1: 🚀 Run Without Domain (Local / IP Based)
### 5️⃣ Build and start services
```bash
docker compose build
docker compose up -d
```

---

# Phase 2A: 🌍 With Domain + SSL (Host Machine Nginx)
### 1️⃣ Install Nginx
```bash
sudo apt update
sudo apt install nginx -y
```

---

### 2️⃣ Create Nginx Config
- Create an Nginx config file /etc/nginx/sites-available/fullstack-app.conf
```nginx
server {
    server_name frontend.myapp.com;
    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

server {
    server_name api.myapp.com;
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

server {
    server_name auth.myapp.com;
    location / {
        proxy_pass http://127.0.0.1:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

# Repeat similar blocks for payments, catalog, analytics, notifications, email, sms, search
```

- Enable the config and reload Nginx
```bash
sudo ln -s /etc/nginx/sites-available/fullstack-app.conf /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

### 3️⃣ Setup SSL with Certbot
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx \
  -d frontend.myapp.com \
  -d api.myapp.com \
  -d auth.myapp.com \
  -d payments.myapp.com \
  -d catalog.myapp.com \
  -d analytics.myapp.com \
  -d notifications.myapp.com \
  -d email.myapp.com \
  -d sms.myapp.com \
  -d search.myapp.com
```

---

### 4️⃣ Access the application
- **Frontend Service** → https://frontend.myapp.com
- **Backend Service** → https://api.myapp.com
- **Auth Service** → https://auth.myapp.com
- **Payments Service** → https://payments.myapp.com
- **Catalog Service** → https://catalog.myapp.com
- **Analytics Service** → https://analytics.myapp.com
- **Notifications Service** → https://notifications.myapp.com
- **Email Service** → https://email.myapp.com
- **SMS Service** → https://sms.myapp.com
- **Search Service** → https://search.myapp.com 

---

# Phase 2B: 🌍 With Domain + SSL (Containerized Nginx)
### 1️⃣ Add Nginx Service in docker-compose.yml
```yml
nginx-proxy:
  image: nginx:latest
  container_name: nginx-proxy
  ports:
    - "80:80"
    - "443:443"
  volumes:
    - ./nginx/conf.d:/etc/nginx/conf.d
    - ./certs:/etc/nginx/certs
  depends_on:
    - frontend-service
    - api-service
    - auth-service
    - payments-service
    - catalog-service
    - analytics-service
    - notifications-service
    - email-service
    - sms-service
    - search-service
```

---

### 2️⃣ Create Nginx Configs (Container Mounted)
- Path: ./nginx/conf.d/fullstack-app.conf
```nginx
server {
    server_name frontend.myapp.com;
    location / {
        proxy_pass http://frontend-service:3000;
    }
}
server {
    server_name api.myapp.com;
    location / {
        proxy_pass http://api-service:8000;
    }
}
server {
    server_name auth.myapp.com;
    location / {
        proxy_pass http://auth-service:8001;
    }
}
# Repeat for payments, catalog, analytics, notifications, email, sms, search
```

---

### 3️⃣ Add SSL Certificates
- Place .crt and .key files inside ./certs directory
- Update Nginx config to enable SSL:
```nginx
server {
    listen 443 ssl;
    server_name frontend.myapp.com;
    ssl_certificate /etc/nginx/certs/frontend.crt;
    ssl_certificate_key /etc/nginx/certs/frontend.key;

    location / {
        proxy_pass http://frontend-service:3000;
    }
}
```

---

### 4️⃣ Start Services
```bash
docker compose up -d
```

---

### 5️⃣ Access Application (HTTPS via Containerized Nginx)
- **Frontend Service** → https://frontend.myapp.com
- **Backend Service** → https://api.myapp.com
- **Auth Service** → https://auth.myapp.com
- **Payments Service** → https://payments.myapp.com
- **Catalog Service** → https://catalog.myapp.com
- **Analytics Service** → https://analytics.myapp.com
- **Notifications Service** → https://notifications.myapp.com
- **Email Service** → https://email.myapp.com
- **SMS Service** → https://sms.myapp.com
- **Search Service** → https://search.myapp.com

---







