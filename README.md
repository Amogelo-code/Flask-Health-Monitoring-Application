# Flask Health Monitoring Application

## Overview

A Python Flask application that provides basic health-check and application information endpoints. The application is containerised using Docker.

## Technologies

- Python
- Flask
- Docker
- Git and GitHub

## Available Endpoints

| Endpoint | Description |
|---|---|
| `/` | Displays a welcome message and environment |
| `/health` | Returns the application health status |
| `/info` | Returns application information and version |

## Running the Application

### Using Docker

Build the image:

```bash
docker build -t flask_app .
```

Run the container:

```bash
docker run -d -p 5000:5000 --name flask-app-container flask_app
```

Access the application at `http://localhost:5000`.

## Future Improvements

- Prometheus monitoring
- Grafana dashboards
- CI/CD with GitHub Actions
- AWS deployment
- Infrastructure as Code with Terraform
