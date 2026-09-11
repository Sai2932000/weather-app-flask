# Dockerized Flask Weather Application

A containerized **Python Flask Weather Application** built to practice Docker containerization, dependency management, image optimization, security, and production-style application execution.

## 🚀 Project Overview

This project takes a Python Flask weather application and packages it into a lightweight, reproducible Docker container.

The application uses a weather API to retrieve current weather information for a requested city and runs behind **Gunicorn** inside the container.

## 🏗️ Architecture

```text
User
  │
  ▼
Browser
  │
  │ Port 8080
  ▼
Docker Container
  │
  ├── Gunicorn
  │
  └── Flask Application
          │
          ▼
      Weather API
      
🛠️ Technologies Used

🐍 Python 3.13
🌐 Flask
🚀 Gunicorn
🐳 Docker
⚡uv
🌦️ Weather API
🐧Linux


### ✨ Key Features

* 🏗️ **Multi-stage Docker build**
* 🐍 **Lightweight `python:3.13-slim` runtime image**
* ⚡ **Fast and reproducible dependency management using `uv`**
* 📦 **Isolated Python virtual environment**
* 🚀 **Gunicorn production WSGI server**
* 🔐 **Non-root container execution**
* ⚙️ **Environment-based configuration**
* 🌐 **Docker port mapping on port `8080`**
* 🌦️ **External Weather API integration**


🐳 Docker Implementation

The Dockerfile uses a multi-stage build:

Build Stage
    │
    ├── Install dependencies
    ├── Create virtual environment
    └── Prepare application
            │
            ▼
Runtime Stage
    │
    ├── Lightweight Python image
    ├── Non-root application user
    ├── Copy required environment
    └── Run with Gunicorn

This approach keeps build dependencies separate from the runtime environment and helps produce a smaller and cleaner final image.

🔐 Security

The container follows basic Docker security practices:

Application runs as a non-root user
API credentials are supplied through environment variables
Sensitive configuration is kept outside the application source code
.env files are excluded from source control

⚙️ Prerequisites

Make sure the following are installed:

Docker
Git
🚀 Run the Application
1. Clone the repository
git clone <your-repository-url>
cd weather-app-flask
2. Create environment configuration

Create a .env file:

WEATHERSTACK_API_KEY=your_api_key

Replace your_api_key with your actual Weatherstack API key.

3. Build the Docker image
docker build -t weather-app-flask .
4. Run the container
docker run -d \
  --name weather_app \
  --env-file .env \
  -p 8080:8080 \
  weather-app-flask
5. Verify the container
docker ps
6. Access the application

Open:

http://localhost:8080

🔍 Useful Docker Commands

View running containers:

docker ps

View application logs:

docker logs weather_app

Stop the container:

docker stop weather_app

Remove the container:

docker rm weather_app

Remove the image:

docker rmi weather-app-flask
📚 What I Learned

This project provided hands-on experience with:

Docker image and container lifecycle
Multi-stage Docker builds
Docker image optimization
Python dependency management with uv
Production WSGI serving with Gunicorn
Non-root container execution
Environment-based application configuration
Docker networking and port mapping
Container troubleshooting and verification
Integrating external APIs with containerized applications

🎯 Project Workflow

Python Flask Application
        ↓
    uv Dependencies
        ↓
  Multi-stage Docker Build
        ↓
   Optimized Docker Image
        ↓
   Docker Container
        ↓
      Gunicorn
        ↓
   Flask Application
        ↓
     Weather API
        ↓
  Weather Information
👨‍💻 Author

Sai Kumar Thumma

DevOps / Cloud Engineer

Skills:

Docker Python Flask Linux AWS GCP Terraform Kubernetes CI/CD