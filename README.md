# System Status Dashboard

A full-stack DevOps project — live server monitoring dashboard deployed on AWS EC2 with a fully automated CI/CD pipeline.

## Live Demo
http://YOUR_EC2_PUBLIC_IP:5000

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
