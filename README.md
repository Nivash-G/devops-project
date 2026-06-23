# System Status Dashboard

A full-stack DevOps project — live server monitoring dashboard deployed on AWS EC2 with a fully automated CI/CD pipeline.

## Live Demo
//184.72.142.23:5000/
> Note: EC2 instance is stopped to avoid AWS charges. 
> To run locally, see instructions below.
## What it does
Displays real-time server metrics from AWS EC2:
- CPU usage
- Memory usage
- Disk usage
- Server uptime

Dashboard auto-refreshes every 5 seconds without page reload.

## Tech Stack
| Tool | Purpose |
|------|---------|
| Python Flask | Backend API serving live metrics |
| Docker | Containerization |
| GitHub Actions | CI/CD pipeline |
| AWS EC2 (Ubuntu) | Cloud deployment |
| Linux | Server management |

## CI/CD Pipeline
Every push to `main` branch automatically:
1. Builds a fresh Docker image
2. Pushes it to Docker Hub
3. SSHes into EC2 and redeploys the container.
## Project Structure
devops-project/

├── app.py                          # Flask backend

├── templates/

│   └── index.html                  # Frontend dashboard

├── Dockerfile                      # Container config

└── .github/

└── workflows/

└── deploy.yml              # CI/CD pipeline
## How to run locally
```bash
git clone https://github.com/Nivash-G/devops-project.git
cd devops-project
pip install flask psutil
python app.py
```
Open http://localhost:5000

## Author
Nivash G — Cloud & DevOps Trainee
[LinkedIn](https://www.linkedin.com/in/nivash-g-05960029b?utm_source=share_via&utm_content=profile&utm_medium=member_android) | [GitHub](https://github.com/Nivash-G)
