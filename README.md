# personal-api

## Overview

This project is a minimal REST API built as part of a DevOps task. It demonstrates how to create, deploy, and manage a simple backend service using Python (Flask), served with Gunicorn, and exposed publicly via an Nginx reverse proxy.

The API contains three endpoints and is deployed on a VPS with persistent uptime.

---

## Tech Stack

* Python (Flask)
* Gunicorn (WSGI server)
* Nginx (reverse proxy)
* Linux (Ubuntu server)

---

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/Hacker-Dark/personal-api.git
cd personal-api
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

App runs on:

```
http://localhost:5000
```

---

## API Endpoints

### 1. GET /

Response:

```json
{
  "message": "API is running"
}
```

---

### 2. GET /health

Response:

```json
{
  "message": "healthy"
}
```

---

### 3. GET /me

Response:

```json
{
  "name": "Mordecai Amehson",
  "email": "amehsonmordecai07@gmail.com",
  "github": "https://github.com/Hacker-Dark"
}
```

---

## Deployment

* Application runs on a private port (5000) using Gunicorn
* Nginx is configured as a reverse proxy to expose the API on port 80
* Service is managed using systemd to ensure it stays running automatically

---

## Live URL

```
http://YOUR_SERVER_IP/
```

(Replace with your actual server IP)

---

## Notes

* All endpoints return:

  * HTTP Status Code: 200
  * Content-Type: application/json
* Response time is under 500ms
* The service runs persistently without manual restarts

---

## Extra

* Use `systemctl status personal-api` to debug if API fails
* Use `sudo nginx -t` before restarting nginx to avoid config errors
* If port 80 fails, check firewall: `sudo ufw allow 'Nginx Full'`
