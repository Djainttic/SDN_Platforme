# SDN Lab Platform - Docker Host Setup Guide

**Version**: 1.0  
**Last Updated**: 2025-11-05  
**Target Audience**: System Administrators, DevOps Engineers

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Server Provisioning](#server-provisioning)
4. [Docker Installation](#docker-installation)
5. [Container Image Building](#container-image-building)
6. [Network Configuration](#network-configuration)
7. [Supabase Integration](#supabase-integration)
8. [Security Configuration](#security-configuration)
9. [Testing](#testing)
10. [Monitoring Setup](#monitoring-setup)
11. [Maintenance](#maintenance)
12. [Troubleshooting](#troubleshooting)

---

## Overview

### Architecture

The SDN Lab Platform uses Docker containers to provide isolated lab environments for each student. The architecture consists of:

- **Frontend**: React web application (already deployed)
- **Supabase Edge Functions**: Backend API for container orchestration
- **Docker Host**: Server running Docker daemon and containers
- **Container Images**: 9 different SDN lab environments

### Communication Flow

```
[Student Browser]
       ↓
[React Frontend] → https://377u4geo9kkl.space.minimax.io
       ↓
[Supabase Edge Functions] → container-orchestrator-production, terminal-stream
       ↓
[Docker Host] → Docker API (unix socket or HTTP)
       ↓
[Docker Containers] → mininet, ryu, ovs, traffic-analyzer, security-lab
```

### Deployment Options

Choose based on scale:

1. **Single Server**: Up to 50 concurrent users
2. **Docker Swarm**: 50-200 concurrent users
3. **Kubernetes**: 200+ concurrent users
4. **Cloud**: Unlimited scale with auto-scaling

This guide focuses on **Single Server** deployment. For Swarm/Kubernetes, see `/workspace/kubernetes-deployment.yml`.

---

## Prerequisites

### System Requirements

**Minimum Specifications**:
- CPU: 4 cores
- RAM: 16 GB
- Storage: 100 GB SSD
- Network: 100 Mbps
- OS: Ubuntu 22.04 LTS

**Recommended Specifications**:
- CPU: 8+ cores
- RAM: 32+ GB
- Storage: 250 GB SSD
- Network: 1 Gbps
- OS: Ubuntu 22.04 LTS

### User Capacity Estimate

Per container resources:
- CPU: 1 core
- RAM: 512 MB
- Disk: 5 GB

**Capacity calculation**:
- Minimum server: ~12 concurrent containers
- Recommended server: ~48 concurrent containers

### Software Requirements

- Ubuntu 22.04 LTS (or Debian 11+)
- Docker CE 24.0+
- Git
- curl/wget
- sudo access

---

## Server Provisioning

### Cloud Providers

#### AWS EC2

```bash
# Instance type: t3.xlarge (4 vCPU, 16 GB RAM)
# or m5.xlarge for production

# Security Group rules:
- SSH (22): Your IP only
- HTTP (80): 0.0.0.0/0
- HTTPS (443): 0.0.0.0/0
- Docker API (2375): Supabase IP ranges only
```

#### Google Cloud Platform

```bash
# Machine type: n2-standard-4 (4 vCPU, 16 GB RAM)

# Firewall rules:
- SSH (22): Your IP
- Docker API (2375): Supabase IPs
```

#### Azure

```bash
# VM size: Standard_D4s_v3 (4 vCPU, 16 GB RAM)

# Network Security Group:
- SSH (22): Your IP
- Docker API (2375): Supabase IPs
```

#### DigitalOcean

```bash
# Droplet: 8 GB Memory / 4 vCPUs / 160 GB SSD
# Cost: ~$48/month

# Firewall:
- SSH (22): Your IP
- Docker API (2375): Supabase IPs (if using HTTP API)
```

### Initial Server Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common git

# Set timezone
sudo timedatectl set-timezone America/New_York

# Configure firewall
sudo ufw allow 22/tcp
sudo ufw enable
```

---

## Docker Installation

### Install Docker Engine

```bash
# Add Docker's official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package index
sudo apt update

# Install Docker Engine
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Verify installation
sudo docker run hello-world
```

### Configure Docker User

```bash
# Add current user to docker group (avoid using sudo)
sudo usermod -aG docker $USER

# Apply group changes (log out and back in, or use newgrp)
newgrp docker

# Verify Docker works without sudo
docker ps
```

### Configure Docker Daemon

Create `/etc/docker/daemon.json`:

```bash
sudo nano /etc/docker/daemon.json
```

Add configuration:

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  },
  "default-address-pools": [
    {
      "base": "172.20.0.0/16",
      "size": 24
    }
  ],
  "storage-driver": "overlay2"
}
```

Restart Docker:

```bash
sudo systemctl restart docker
```

---

## Container Image Building

### Clone Project Repository

```bash
# Create working directory
mkdir -p ~/sdn-lab-platform
cd ~/sdn-lab-platform

# Option 1: If you have the workspace files
# Copy the entire workspace to the server

# Option 2: Get files from deployed location
# Download Dockerfile and compose files
```

### Build Container Images

Navigate to the sdn_lab directory where Dockerfiles are located:

```bash
cd ~/sdn-lab-platform/sdn_lab

# Build all images using docker-compose
docker-compose build

# This builds:
# - sdn-mininet:latest
# - sdn-ryu:latest
# - sdn-ovs:latest
# - sdn-traffic:latest
# - sdn-security:latest
```

### Verify Images

```bash
# List built images
docker images | grep sdn-

# Expected output:
# sdn-mininet          latest    xxx    xxx    xxxMB
# sdn-ryu              latest    xxx    xxx    xxxMB
# sdn-ovs              latest    xxx    xxx    xxxMB
# sdn-traffic          latest    xxx    xxx    xxxMB
# sdn-security         latest    xxx    xxx    xxxMB
```

### Test Image

```bash
# Test mininet image
docker run --rm --privileged sdn-mininet:latest mn --version

# Expected output: mininet 2.x.x

# Test RYU image
docker run --rm sdn-ryu:latest ryu-manager --version

# Expected output: ryu-manager x.x
```

---

## Network Configuration

### Create Docker Network

```bash
# Create dedicated network for SDN labs
docker network create sdn-lab-network

# Verify network
docker network ls | grep sdn-lab
```

### Configure Docker API Access

Choose ONE of the following methods:

#### Option A: Unix Socket (Recommended - Same Server)

If Supabase Edge Functions run on the same server:

```bash
# Edge functions need access to /var/run/docker.sock
# Ensure Docker socket has correct permissions
sudo chmod 666 /var/run/docker.sock

# Or use socket proxy (more secure)
docker run -d \
  --name docker-socket-proxy \
  --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -p 127.0.0.1:2375:2375 \
  tecnativa/docker-socket-proxy
```

Set environment variable in Supabase:
```
DOCKER_HOST=unix:///var/run/docker.sock
```

#### Option B: HTTP API (Remote Server)

If Edge Functions are remote:

Edit `/etc/docker/daemon.json`:

```json
{
  "hosts": [
    "unix:///var/run/docker.sock",
    "tcp://0.0.0.0:2375"
  ],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

Create override for systemd:

```bash
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo nano /etc/systemd/system/docker.service.d/override.conf
```

Add:

```ini
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd
```

Restart Docker:

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

**CRITICAL**: Secure the API endpoint:

```bash
# Allow only Supabase IP ranges
# Get Supabase IP ranges from their documentation

sudo ufw allow from SUPABASE_IP_RANGE to any port 2375
sudo ufw deny 2375
```

Set environment variable in Supabase:
```
DOCKER_HOST=http://YOUR_SERVER_IP:2375
```

---

## Supabase Integration

### Set Environment Variable

1. Log in to Supabase Dashboard: https://supabase.com/dashboard
2. Navigate to your project: `zwtjirdodmupjsissjzr`
3. Go to **Project Settings** → **Edge Functions** → **Environment Variables**
4. Add new variable:
   - **Key**: `DOCKER_HOST`
   - **Value**: 
     - Unix socket: `unix:///var/run/docker.sock`
     - HTTP API: `http://YOUR_SERVER_IP:2375`
5. Save changes

### Redeploy Edge Functions

After setting `DOCKER_HOST`, redeploy functions to apply changes:

```bash
# The functions are already deployed, but to update environment:
# 1. Go to Supabase Dashboard
# 2. Navigate to Edge Functions
# 3. Click "Redeploy" on both:
#    - container-orchestrator-production
#    - terminal-stream
```

---

## Security Configuration

### Container Security

Implement security best practices:

```bash
# Enable user namespaces
sudo nano /etc/docker/daemon.json
```

Add to configuration:

```json
{
  "userns-remap": "default",
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

Restart Docker:

```bash
sudo systemctl restart docker
```

### Network Security

```bash
# Configure firewall
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow from SUPABASE_IP to any port 2375  # If using HTTP API
sudo ufw enable

# Verify rules
sudo ufw status
```

### Container Resource Limits

Already implemented in edge function code:

- CPU: 1 core per container
- Memory: 512 MB per container
- Disk: 5 GB per container
- PIDs: 100 per container

### Regular Updates

```bash
# Schedule automatic security updates
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades

# Update Docker images monthly
# Create cron job
crontab -e
```

Add:

```bash
0 2 1 * * cd /path/to/sdn_lab && docker-compose build --pull
```

---

## Testing

### Test Container Creation

```bash
# Test manual container creation
docker run -d \
  --name test-mininet \
  --network sdn-lab-network \
  --privileged \
  --memory=512m \
  --cpus=1 \
  sdn-mininet:latest sleep 3600

# Verify container is running
docker ps | grep test-mininet

# Execute command in container
docker exec test-mininet mn --version

# Check logs
docker logs test-mininet

# Clean up
docker rm -f test-mininet
```

### Test Docker API

#### Unix Socket Test

```bash
curl --unix-socket /var/run/docker.sock http://localhost/version
```

Expected: JSON with Docker version info

#### HTTP API Test

```bash
curl http://localhost:2375/version
```

Expected: JSON with Docker version info

### Test End-to-End

1. Open platform: https://377u4geo9kkl.space.minimax.io
2. Log in with test credentials
3. Navigate to any lab section → Terminal tab
4. Click "Start Container"
5. Wait for container to start
6. Execute command: `mn --version`
7. Verify output appears in terminal
8. Click "Stop Container"
9. Verify container is stopped: `docker ps`

---

## Monitoring Setup

### Basic Monitoring

Monitor container metrics:

```bash
# View running containers
docker ps

# View container stats (real-time)
docker stats

# View system resources
docker system df

# View logs
docker logs <container_id>
```

### Prometheus & Grafana (Optional but Recommended)

Deploy monitoring stack:

```bash
# Create monitoring docker-compose.yml
nano ~/monitoring/docker-compose.yml
```

Content:

```yaml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    restart: always

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana-data:/var/lib/grafana
    restart: always

  node-exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"
    restart: always

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    ports:
      - "8080:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    restart: always

volumes:
  prometheus-data:
  grafana-data:
```

Start monitoring:

```bash
cd ~/monitoring
docker-compose up -d
```

Access:
- Prometheus: http://YOUR_SERVER_IP:9090
- Grafana: http://YOUR_SERVER_IP:3000 (admin/admin)
- Node Exporter: http://YOUR_SERVER_IP:9100
- cAdvisor: http://YOUR_SERVER_IP:8080

### Alerting

Configure alerts in Prometheus:

```yaml
# prometheus.yml
rule_files:
  - 'alerts.yml'

alerting:
  alertmanagers:
    - static_configs:
      - targets: ['localhost:9093']
```

Create `alerts.yml`:

```yaml
groups:
  - name: container_alerts
    rules:
      - alert: HighContainerCount
        expr: count(container_last_seen) > 40
        for: 5m
        annotations:
          summary: "High number of containers running"
          
      - alert: HighCPUUsage
        expr: rate(process_cpu_seconds_total[1m]) > 0.8
        for: 5m
        annotations:
          summary: "High CPU usage detected"
```

---

## Maintenance

### Daily Tasks

```bash
# Check container count
docker ps -q | wc -l

# Check disk usage
docker system df

# View logs for errors
docker events --since 24h | grep error
```

### Weekly Tasks

```bash
# Clean up stopped containers
docker container prune -f

# Clean up unused networks
docker network prune -f

# Clean up unused images
docker image prune -a -f

# Clean up volumes (CAREFUL - preserves active data)
docker volume prune -f
```

### Monthly Tasks

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Rebuild container images
cd ~/sdn-lab-platform/sdn_lab
docker-compose build --pull

# Update Docker engine
sudo apt update && sudo apt install docker-ce docker-ce-cli containerd.io

# Review logs for issues
journalctl -u docker --since "30 days ago" | grep error

# Check security updates
sudo unattended-upgrades --dry-run
```

### Backup

```bash
# Backup Docker images
docker save sdn-mininet:latest | gzip > sdn-mininet-backup.tar.gz

# Backup Docker volumes (if used)
docker run --rm -v sdn-data:/data -v $(pwd):/backup ubuntu tar czf /backup/sdn-data-backup.tar.gz /data

# Backup configuration files
tar czf docker-config-backup.tar.gz /etc/docker/ ~/sdn-lab-platform/
```

---

## Troubleshooting

### Container Won't Start

**Symptoms**: Edge function returns "Failed to create container"

**Diagnosis**:
```bash
# Check Docker daemon
sudo systemctl status docker

# Check available resources
free -h
df -h

# Check for stuck containers
docker ps -a

# Check Docker logs
sudo journalctl -u docker -n 100
```

**Solutions**:
1. Restart Docker: `sudo systemctl restart docker`
2. Clean up containers: `docker container prune -f`
3. Check disk space: `df -h` (need at least 10GB free)
4. Increase resource limits if needed

### High Resource Usage

**Symptoms**: Slow performance, containers crashing

**Diagnosis**:
```bash
# Check overall system resources
top
htop  # Install: sudo apt install htop

# Check Docker stats
docker stats --no-stream

# Check container count
docker ps -q | wc -l

# Check memory
free -h
```

**Solutions**:
1. Stop inactive containers: Find and stop old sessions
2. Implement auto-cleanup cron job
3. Increase server resources (upgrade instance)
4. Reduce max concurrent containers

### Network Issues

**Symptoms**: Containers can't communicate, no internet access

**Diagnosis**:
```bash
# Check Docker networks
docker network ls
docker network inspect sdn-lab-network

# Test container networking
docker run --rm --network sdn-lab-network alpine ping -c 3 google.com

# Check iptables rules
sudo iptables -L -n
```

**Solutions**:
1. Recreate network: `docker network rm sdn-lab-network && docker network create sdn-lab-network`
2. Restart Docker: `sudo systemctl restart docker`
3. Check firewall: `sudo ufw status`
4. Verify DNS: `cat /etc/resolv.conf`

### Docker API Connection Failed

**Symptoms**: Edge function can't connect to Docker API

**Diagnosis**:
```bash
# Test local connection
curl --unix-socket /var/run/docker.sock http://localhost/version

# Or for HTTP API
curl http://localhost:2375/version

# Check if Docker is listening
sudo netstat -tlnp | grep docker

# Check permissions
ls -l /var/run/docker.sock
```

**Solutions**:
1. Verify `DOCKER_HOST` environment variable in Supabase
2. Check firewall rules: `sudo ufw status`
3. Verify Docker daemon config: `cat /etc/docker/daemon.json`
4. Restart Docker: `sudo systemctl restart docker`
5. Check Supabase can reach server (network connectivity)

### Image Build Failures

**Symptoms**: `docker-compose build` fails

**Diagnosis**:
```bash
# Check Dockerfile syntax
docker build -t test -f Dockerfile .

# Check available disk space
df -h

# Check build logs
docker-compose build --no-cache 2>&1 | tee build.log
```

**Solutions**:
1. Free up disk space
2. Pull base images manually: `docker pull ubuntu:22.04`
3. Build without cache: `docker-compose build --no-cache`
4. Check Dockerfile for errors

### Permission Denied Errors

**Symptoms**: "permission denied" when accessing Docker

**Diagnosis**:
```bash
# Check user groups
groups $USER

# Check Docker socket permissions
ls -l /var/run/docker.sock
```

**Solutions**:
```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Apply group changes
newgrp docker

# Or reboot server
sudo reboot
```

---

## Appendix

### Quick Reference Commands

```bash
# Container management
docker ps                          # List running containers
docker ps -a                       # List all containers
docker stop <container_id>         # Stop container
docker rm <container_id>           # Remove container
docker logs <container_id>         # View logs

# Image management
docker images                      # List images
docker rmi <image_id>              # Remove image
docker pull <image>                # Pull image
docker build -t <name> .           # Build image

# Resource monitoring
docker stats                       # Real-time stats
docker system df                   # Disk usage
docker top <container_id>          # Container processes

# Network management
docker network ls                  # List networks
docker network inspect <network>   # Network details
docker network create <network>    # Create network

# Cleanup
docker system prune -a             # Clean everything (CAREFUL)
docker container prune -f          # Remove stopped containers
docker image prune -a -f           # Remove unused images
```

### Docker Compose Commands

```bash
# Build images
docker-compose build

# Build without cache
docker-compose build --no-cache

# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs

# Scale service
docker-compose up -d --scale service=3
```

### System Information

```bash
# Docker version
docker --version
docker version

# System info
docker info

# Disk usage
docker system df -v

# Resource limits
docker info | grep -i cpu
docker info | grep -i memory
```

### Performance Tuning

**Increase container limits** (in edge function code):
```javascript
Memory: 1073741824,  // 1GB instead of 512MB
NanoCpus: 2000000000,  // 2 CPUs instead of 1
```

**Optimize Docker daemon**:
```json
{
  "default-ulimits": {
    "nofile": {
      "Name": "nofile",
      "Hard": 64000,
      "Soft": 64000
    }
  }
}
```

### Cost Estimates

**Monthly Costs** (estimated):

| Provider | Instance | vCPU | RAM | Storage | Cost |
|----------|----------|------|-----|---------|------|
| AWS EC2 | t3.xlarge | 4 | 16GB | 100GB | $120 |
| GCP | n2-standard-4 | 4 | 16GB | 100GB | $140 |
| Azure | D4s_v3 | 4 | 16GB | 100GB | $150 |
| DigitalOcean | 4-vCPU | 4 | 16GB | 160GB | $84 |

Add monitoring costs if using cloud-native tools.

---

**End of Docker Host Setup Guide**

For platform usage, refer to Professor User Guide and Student User Guide.

**Version**: 1.0  
**Last Updated**: 2025-11-05  
**Document Version**: 1.0
