# Dockerized Entertainment Service (Nomad Cosmic)

![Docker Cloud Automated build](https://img.shields.io/badge/docker-automated-blue?logo=docker)
![GitHub Actions CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-brightgreen?logo=github-actions)
![AWS Deployment](https://img.shields.io/badge/AWS-EC2%20Deployment-orange?logo=amazon-aws)

This project serves as a comprehensive demonstration of modern **DevOps, Containerization, and Microservice Architecture**. It features a glassmorphism-themed frontend connected seamlessly to a Python AI processing backend.

## Architecture Overview
The system is constructed using an industry-standard segregated microservices approach:

1. **Frontend Service (`frontend.Dockerfile`)**: 
   * Features a stunning, zero-dependency HTML/CSS/JS glassmorphism interface.
   * Containerized using a multi-stage optimized strategy leveraging **Nginx (Alpine)** for lightning-fast delivery and strict security routing.
2. **Backend Engine (`backend.Dockerfile`)**:
   * A Python structural skeleton utilizing **FastAPI** and **Pydantic** designed heavily for data validation.
   * Serves as the processing node for future Groq/Gemini Multi-Agent API calls.
3. **Orchestration (`docker-compose.yml`)**:
   * Bridges the isolated containers onto a private internal Docker bridge network (`nomad_network`).

## Continuous Integration / Deployment (CI/CD)
This repository is fully wired to an automated GitHub Actions pipeline (`.github/workflows/deploy.yml`). 
* **The CI Trigger:** Upon every `git push` to the `main` branch, specialized GitHub servers intercept the event.
* **The Build Phase:** It automatically compiles both the latest Frontend and Backend Dockerfiles simultaneously.
* **Registry Push:** It uses encrypted GitHub Secrets to securely authenticate and push the fully updated images to the public Docker Hub Registry, ensuring 100% cloud portability.

## Local Execution Instructions

To spin up the entire architecture on any computer locally without requiring Node or Python installations:

1. Ensure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and running.
2. Clone this repository to your terminal.
3. Execute the orchestrator:
```bash
docker-compose up --build -d
```
4. Access the gorgeous visual UI locally via `http://localhost:80/`

## AWS Cloud Deployment Summary
This project is currently deployed and verified on an **AWS Amazon Linux EC2** instance via `t3.micro`. 

**(AWS Deployment Commands History):**
```bash
sudo yum install docker-buildx-plugin docker-compose-plugin git -y
sudo service docker start
git clone [repository_link]
cd [repository_name]
docker compose up --build -d
```
