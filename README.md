# DevOps Order Application

A Python-based web application with a basic CI/CD pipeline implemented using **GitHub, Jenkins, and Docker**.

The project automates application validation, Docker image creation, container deployment, and deployment verification.

## Technologies Used

* Python
* Git
* GitHub
* Jenkins
* Docker
* CI/CD

## Project Workflow

```text
Developer
    ↓
GitHub Repository
    ↓
Jenkins
    ↓
Test
    ↓
Build Docker Image
    ↓
Deploy Docker Container
    ↓
Verify Deployment
    ↓
Application Running on Port 5000
```

## CI/CD Pipeline

The Jenkins pipeline contains four main stages:

### 1. Test

Jenkins first checks whether the required application files are available.

```bash
test -f app.py
test -f database.py
test -f Dockerfile
test -f requirements.txt
```

If any required file is missing, the pipeline fails.

If all files are available, Jenkins continues to the next stage.

> Note: This project currently performs basic file validation rather than automated unit testing.

### 2. Build Docker Image

Jenkins builds the application into a Docker image using the Dockerfile.

```bash
docker build -t devops-order-app:1.0 .
```

The Docker image contains the application code, Python environment, and required dependencies.

The image created is:

```text
devops-order-app:1.0
```

### 3. Deploy

Jenkins uses the Docker image to create and run a container.

```bash
docker rm -f devops-order-app
docker run -d --name devops-order-app -p 5000:5000 devops-order-app:1.0
```

The container runs the Python application and maps:

```text
Host Port 5000 → Container Port 5000
```

The application can then be accessed through:

```text
http://localhost:5000
```

### 4. Verify Deployment

Jenkins checks whether the application container is running.

```bash
docker ps --filter name=devops-order-app
```

If the container is running successfully, the deployment verification is completed.

## Dockerfile

The application is containerized using the following Dockerfile:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Dockerfile Explanation

* `FROM` → Uses Python 3.11 slim as the base image.
* `WORKDIR` → Sets `/app` as the working directory.
* `COPY requirements.txt` → Copies dependency file into the image.
* `RUN pip install` → Installs Python dependencies.
* `COPY . .` → Copies the application source code.
* `EXPOSE 5000` → Documents the application port.
* `CMD` → Starts the application using `python app.py`.

## Why GitHub?

GitHub is used to store and manage the application source code and Jenkinsfile.

When the pipeline runs, Jenkins checks out the latest code from the GitHub repository.

## Why Jenkins?

Jenkins automates the CI/CD process.

Without Jenkins, we would manually perform:

```text
Test
 ↓
Build Docker Image
 ↓
Run Docker Container
 ↓
Verify Application
```

Jenkins performs these steps automatically as part of the pipeline.

## Why Docker?

Docker packages the application and its dependencies into a Docker image.

The same image can then be used to create a container and run the application consistently.

This reduces dependency and environment-related issues when running the application on another machine.

## CI and CD in This Project

### Continuous Integration (CI)

The CI part includes:

```text
GitHub Code
    ↓
Jenkins Checkout
    ↓
File Validation
    ↓
Docker Image Build
```

### Continuous Deployment (CD)

The CD part includes:

```text
Docker Image
    ↓
Docker Container
    ↓
Application Deployment
    ↓
Deployment Verification
```

Therefore, this project demonstrates a basic **CI/CD workflow using Jenkins and Docker**.

## Application Deployment

The application is deployed as a Docker container:

```text
Docker Image
devops-order-app:1.0
       ↓
Docker Container
devops-order-app
       ↓
Port 5000
       ↓
Python Application
```

The application is accessed using:

```text
http://localhost:5000
```

## Jenkins + Docker Setup

Jenkins runs inside a Docker container.

A separate Docker-in-Docker container is used as the Docker daemon for Jenkins.

```text
Jenkins Container
       ↓
Docker Client
       ↓
Docker-in-Docker (DinD)
       ↓
Docker Image
       ↓
Application Container
```

Jenkins communicates with the Docker daemon using:

```text
DOCKER_HOST=tcp://jenkins-docker:2375
```

This allows Jenkins to build Docker images and create application containers.

## Result

The final pipeline successfully performs:

```text
GitHub
  ↓
Jenkins
  ↓
Test
  ↓
Docker Image Build
  ↓
Docker Container Deployment
  ↓
Deployment Verification
  ↓
Application Running
```

## Project Outcome

This project demonstrates practical knowledge of:

* Git and GitHub
* Jenkins CI/CD pipelines
* Jenkinsfile
* Dockerfile
* Docker image creation
* Docker container deployment
* Port mapping
* Basic deployment verification
* Jenkins and Docker integration


