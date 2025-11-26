# To-Do List CLI Application (Jenkins + Docker CI/CD)

## Overview
This is a simple **To-Do List CLI Application** written in Python.  
It includes automated **testing, Docker packaging, and CI/CD using Jenkins**.

This project was created as part of the assignment:

- Pull code from GitHub
- Build the project
- Run tests automatically
- If tests pass → build Docker image
- Push image to Docker Hub using Jenkins Pipeline

---

## Project Structure

todo-app/
│── app.py
│── test_app.py
│── requirements.txt
│── Dockerfile
└── Jenkinsfile


---

## Running Locally

1. Install dependencies:

pip install -r requirements.txt


2. Run the app:

python app.py


3. Run tests:

pytest


---

## Docker Commands

Build image:

docker build -t username/appname .


Run image:

docker run -it username/appname


---

## Jenkins Pipeline Stages

1. **Clone Repository**  
2. **Install Dependencies**  
3. **Run Pytest Tests**  
4. **Build Docker Image**  
5. **Authenticate to Docker Hub**  
6. **Push Image to Docker Hub**  

---

## Requirements

- Python 3.10
- pytest
- Docker
- Jenkins (running inside WSL2)

---

## Automated CI/CD
When a new commit is pushed to GitHub:
- Jenkins automatically pulls the code  
- Runs all tests  
- Builds a Docker container  
- Pushes the final image to Docker Hub 
