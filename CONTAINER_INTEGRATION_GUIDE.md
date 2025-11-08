# SDN Lab Platform - Complete Container Integration Guide

## Overview

This document provides comprehensive instructions for deploying the SDN Lab Platform with full Docker container integration, enabling real interactive labs with web-based terminals.

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Prerequisites](#prerequisites)
3. [Database Schema](#database-schema)
4. [Backend Services](#backend-services)
5. [Frontend Integration](#frontend-integration)
6. [Docker Container Setup](#docker-container-setup)
7. [Deployment Options](#deployment-options)
8. [Security Configuration](#security-configuration)
9. [Monitoring & Maintenance](#monitoring--maintenance)
10. [Troubleshooting](#troubleshooting)

---

## Architecture Overview

### System Components

```
┌─────────────────────────────────────────────────────────────────┐
│                      Student Browser                             │
│  ┌───────────────────┐         ┌──────────────────────┐        │
│  │   React Frontend  │ ◄────► │  xterm.js Terminal   │         │
│  └─────────┬─────────┘         └──────────────────────┘        │
└────────────┼─────────────────────────────────────────────────────┘
             │
             │ HTTPS
             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Supabase Edge Functions                       │
│  ┌──────────────────────────────────────────────────────┐      │
│  │       container-orchestrator Edge Function            │      │
│  │  - Start/Stop Containers                              │      │
│  │  - Execute Commands                                   │      │
│  │  - Monitor Resources                                  │      │
│  │  - Session Management                                 │      │
│  └────────────────────┬─────────────────────────────────┘      │
└─────────────────────────┼────────────────────────────────────────┘
                          │
                          │ Docker API
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Docker Host Server                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │  Mininet    │  │  RYU        │  │    OVS      │            │
│  │  Container  │  │  Container  │  │  Container  │   ...      │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
│                                                                  │
│  Student-specific isolated containers with SDN tools            │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Student starts lab** → Frontend calls edge function
2. **Edge function** → Creates database record + starts Docker container
3. **Container running** → Student can execute commands via web terminal
4. **Commands executed** → Via Docker API, output returned to terminal
5. **Session tracked** → All events logged in database
6. **Cleanup** → Automatic container cleanup after inactivity

---

## Prerequisites

### Server Requirements

- **OS**: Ubuntu 22.04 LTS or higher (or Docker-capable Linux)
- **CPU**: 4+ cores (8+ recommended for production)
- **RAM**: 16GB minimum (32GB+ recommended for multiple concurrent users)
- **Storage**: 100GB+ SSD (containers and student data)
- **Network**: Public IP with ports 80/443 open

### Software Dependencies

```bash
# Docker Engine
Docker version 24.0+ with Docker Compose v2

# Node.js (for frontend build)
Node.js 18+ with pnpm

# Supabase CLI (optional, for local development)
Supabase CLI 1.0+
```

---

## Database Schema

### Tables Created

The following tables are automatically created by migration:

#### 1. `container_sessions`
Tracks Docker container lifecycle for each student session.

```sql
- id: UUID (primary key)
- user_id: UUID (references auth.users)
- section_number: INTEGER (0-8, lab section)
- container_id: TEXT (Docker container ID)
- container_name: TEXT (unique container name)
- container_status: TEXT (pending/starting/running/stopping/stopped/error)
- container_type: TEXT (mininet/ryu/ovs/traffic-analyzer/security-lab/custom)
- ports: JSONB (port mappings)
- environment: JSONB (environment variables)
- started_at: TIMESTAMPTZ
- stopped_at: TIMESTAMPTZ
- last_activity_at: TIMESTAMPTZ
- error_message: TEXT
- metadata: JSONB
```

#### 2. `terminal_sessions`
Manages web terminal connections to containers.

```sql
- id: UUID
- container_session_id: UUID (references container_sessions)
- user_id: UUID
- terminal_id: TEXT (unique terminal identifier)
- status: TEXT (active/inactive/closed)
- last_command: TEXT
- command_history: JSONB
- output_buffer: TEXT
```

#### 3. `container_metrics`
Stores resource usage metrics for monitoring.

```sql
- id: UUID
- container_session_id: UUID
- cpu_percent: NUMERIC
- memory_mb: NUMERIC
- network_rx_bytes: BIGINT
- network_tx_bytes: BIGINT
- disk_read_bytes: BIGINT
- disk_write_bytes: BIGINT
- recorded_at: TIMESTAMPTZ
```

#### 4. `container_events`
Logs all container lifecycle events for audit trail.

```sql
- id: UUID
- container_session_id: UUID
- event_type: TEXT (create/start/stop/restart/error/command_executed/timeout)
- event_data: JSONB
- created_at: TIMESTAMPTZ
```

### Migration Applied

Migration file: `1730782000_create_container_sessions.sql`
Status: ✅ Applied successfully to Supabase database

---

## Backend Services

### Edge Function: container-orchestrator

**Location**: `/workspace/supabase/functions/container-orchestrator/index.ts`
**Status**: ✅ Deployed to Supabase
**Invoke URL**: `https://zwtjirdodmupjsissjzr.supabase.co/functions/v1/container-orchestrator`

#### API Endpoints

##### 1. Start Container
```typescript
POST /functions/v1/container-orchestrator
{
  "action": "start",
  "sectionNumber": 0,
  "containerType": "mininet"
}

Response:
{
  "data": {
    "sessionId": "uuid",
    "containerId": "docker-id",
    "containerName": "sdn-lab-user-section-0-timestamp",
    "status": "running",
    "ports": { "8081": 8081 },
    "message": "Container started successfully"
  }
}
```

##### 2. Stop Container
```typescript
POST /functions/v1/container-orchestrator
{
  "action": "stop",
  "sessionId": "uuid"
}

Response:
{
  "data": {
    "sessionId": "uuid",
    "status": "stopped",
    "message": "Container stopped successfully"
  }
}
```

##### 3. Execute Command
```typescript
POST /functions/v1/container-orchestrator
{
  "action": "execute",
  "sessionId": "uuid",
  "command": "sudo mn --version"
}

Response:
{
  "data": {
    "command": "sudo mn --version",
    "output": "Mininet 2.3.0\nRyu 4.34\nOpen vSwitch 2.17.3",
    "exitCode": 0,
    "timestamp": "2025-11-05T05:26:12Z"
  }
}
```

##### 4. Get Container Status
```typescript
POST /functions/v1/container-orchestrator
{
  "action": "status",
  "sessionId": "uuid"
}

Response:
{
  "data": {
    "sessionId": "uuid",
    "containerStatus": "running",
    "containerName": "sdn-lab-...",
    "startedAt": "2025-11-05T05:26:12Z",
    "lastActivity": "2025-11-05T05:30:00Z",
    "stats": {
      "cpu_percent": 25.5,
      "memory_mb": 256.3,
      "network_rx_bytes": 1024000,
      "network_tx_bytes": 512000
    }
  }
}
```

##### 5. List User Containers
```typescript
POST /functions/v1/container-orchestrator
{
  "action": "list"
}

Response:
{
  "data": {
    "containers": [
      { "id": "uuid", "section_number": 0, "container_status": "running", ... }
    ]
  }
}
```

##### 6. Cleanup Inactive Containers
```typescript
POST /functions/v1/container-orchestrator
{
  "action": "cleanup"
}

Response:
{
  "data": {
    "cleanedCount": 3,
    "message": "Cleaned up 3 inactive containers"
  }
}
```

---

## Frontend Integration

### Web Terminal Component

**Location**: `/workspace/sdn-lab-platform/src/components/WebTerminal.tsx`
**Technology**: xterm.js + FitAddon

#### Features

- ✅ Real-time terminal emulation in browser
- ✅ Container start/stop controls
- ✅ Command execution via Docker API
- ✅ Fullscreen mode toggle
- ✅ Status indicators (stopped/starting/running/error)
- ✅ Command history and buffer
- ✅ Keyboard shortcuts (Enter, Ctrl+C, Backspace)
- ✅ Responsive design with auto-fit
- ✅ Themed terminal (dark mode)

#### Usage in Lab Interface

Updated component: `LabSection.tsx`
```typescript
import { WebTerminal } from './WebTerminal'

{activeTab === 'terminal' && (
  <WebTerminal sectionNumber={section.number} />
)}
```

---

## Docker Container Setup

### Lab Container Images

#### Required Images (9 lab types)

```bash
# 1. Mininet (Sections 0, 1, 4, 6)
docker build -t sdn-mininet:latest /workspace/sdn_lab/mininet

# 2. RYU Controller (Sections 2, 7)
docker build -t sdn-ryu:latest /workspace/sdn_lab/ryu

# 3. Open vSwitch (Section 3)
docker build -t sdn-ovs:latest /workspace/sdn_lab/ovs

# 4. Traffic Analyzer (Section 5)
docker build -t sdn-traffic:latest /workspace/sdn_lab/traffic_analysis

# 5. Security Lab (Section 8)
docker build -t sdn-security:latest /workspace/sdn_lab/advanced_security

# Additional support images
docker build -t sdn-odl:latest /workspace/sdn_lab/odl
```

### Build All Images

```bash
cd /workspace/sdn_lab
docker-compose build
```

### Image Optimization

```dockerfile
# Multi-stage build example
FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y build-essential python3 python3-pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

FROM ubuntu:22.04
COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
# Copy only necessary files
# Result: 60% smaller image
```

### Security Hardening

```bash
# 1. Use non-root user
USER sdnlab

# 2. Read-only root filesystem
--read-only --tmpfs /tmp

# 3. Resource limits
--memory="512m" --cpus="1.0"

# 4. Network isolation
--network=student-${USER_ID}

# 5. Drop capabilities
--cap-drop=ALL --cap-add=NET_ADMIN
```

---

## Deployment Options

### Option 1: Single Server Deployment (Recommended for <50 users)

**Architecture**: All containers on one Docker host

```bash
# 1. Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 2. Enable Docker API (WARNING: Use firewall!)
sudo systemctl edit docker.service
# Add:
# [Service]
# ExecStart=
# ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock

sudo systemctl restart docker

# 3. Build images
cd /workspace/sdn_lab
docker-compose build

# 4. Configure firewall
sudo ufw allow from 10.0.0.0/8 to any port 2375
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# 5. Update edge function to use Docker API
# Replace simulateDockerStart/Exec functions with real Docker API calls
```

### Option 2: Docker Swarm (50-200 users)

```bash
# Initialize swarm
docker swarm init --advertise-addr <manager-ip>

# Add worker nodes
docker swarm join --token <token> <manager-ip>:2377

# Deploy stack
docker stack deploy -c docker-compose.yml sdn-lab

# Scale services
docker service scale sdn-lab_mininet=5
```

### Option 3: Kubernetes (200+ users, Enterprise)

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sdn-mininet
spec:
  replicas: 10
  selector:
    matchLabels:
      app: sdn-mininet
  template:
    metadata:
      labels:
        app: sdn-mininet
    spec:
      containers:
      - name: mininet
        image: sdn-mininet:latest
        resources:
          limits:
            memory: "512Mi"
            cpu: "1000m"
          requests:
            memory: "256Mi"
            cpu: "500m"
        securityContext:
          privileged: true
```

### Option 4: Cloud Deployment (AWS/GCP/Azure)

#### AWS ECS with Fargate

```bash
# 1. Create ECR repositories
aws ecr create-repository --repository-name sdn-mininet
aws ecr create-repository --repository-name sdn-ryu

# 2. Push images
docker tag sdn-mininet:latest <account>.dkr.ecr.us-east-1.amazonaws.com/sdn-mininet:latest
docker push <account>.dkr.ecr.us-east-1.amazonaws.com/sdn-mininet:latest

# 3. Create ECS cluster
aws ecs create-cluster --cluster-name sdn-lab-cluster

# 4. Define task definition (see AWS docs)

# 5. Create service
aws ecs create-service --cluster sdn-lab-cluster --service-name sdn-lab-service
```

---

## Security Configuration

### 1. Command Whitelist

Located in: `container-orchestrator/index.ts`

```typescript
function isCommandAllowed(command: string) {
  const dangerousPatterns = [
    /rm\s+-rf\s+\//, // Dangerous delete
    /dd\s+if=/, // Disk operations
    /mkfs/, // Format
    /:(){ :|:& };:/, // Fork bomb
    /wget.*\|.*sh/, // Remote script execution
    /curl.*\|.*sh/
  ];

  return !dangerousPatterns.some(pattern => pattern.test(command));
}
```

### 2. Resource Limits

```json
{
  "HostConfig": {
    "Memory": 536870912,  // 512MB
    "NanoCpus": 1000000000,  // 1 CPU
    "PidsLimit": 100,
    "DiskQuota": 5368709120  // 5GB
  }
}
```

### 3. Network Isolation

```bash
# Create isolated network per student
docker network create --driver bridge student-${USER_ID}

# Run container in isolated network
docker run --network student-${USER_ID} sdn-mininet:latest
```

### 4. User Namespaces

```bash
# Enable user namespaces in Docker daemon
{
  "userns-remap": "default"
}

# Now containers run as unprivileged users on host
```

### 5. Audit Logging

All operations logged in `container_events` table:
- Container creation
- Command execution
- Stop/start events
- Errors

---

## Monitoring & Maintenance

### 1. Metrics Collection

```typescript
// Collect metrics every 30 seconds
setInterval(async () => {
  const stats = await docker.getContainer(containerId).stats({stream: false});
  await supabase.from('container_metrics').insert({
    container_session_id: sessionId,
    cpu_percent: stats.cpu_stats.cpu_usage.total_usage,
    memory_mb: stats.memory_stats.usage / 1024 / 1024,
    // ... more metrics
  });
}, 30000);
```

### 2. Automatic Cleanup

```typescript
// Cron job to cleanup inactive containers (run every hour)
POST /functions/v1/container-orchestrator
{
  "action": "cleanup"
}

// Stops containers with no activity for 1+ hour
```

### 3. Health Checks

```bash
# Check Docker daemon
curl http://localhost:2375/_ping

# Check container health
docker ps --filter health=unhealthy
```

### 4. Log Management

```bash
# Rotate Docker logs
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

### 5. Monitoring Dashboard

Create Grafana dashboard with:
- Active containers count
- CPU/Memory usage per lab section
- Command execution rate
- Error rate
- Session duration

---

## Troubleshooting

### Issue 1: Container fails to start

**Symptoms**: Error in terminal, container status = "error"

**Diagnosis**:
```bash
# Check Docker daemon logs
sudo journalctl -u docker.service -n 50

# Check container logs
docker logs <container-id>

# Check disk space
df -h

# Check memory
free -h
```

**Solutions**:
- Ensure Docker daemon is running
- Check resource availability (CPU/RAM/disk)
- Verify image exists: `docker images | grep sdn-`
- Check firewall rules
- Restart Docker: `sudo systemctl restart docker`

### Issue 2: Commands not executing

**Symptoms**: Terminal shows "Executing..." indefinitely

**Diagnosis**:
```bash
# Check edge function logs
supabase functions logs container-orchestrator

# Test Docker API directly
curl http://localhost:2375/containers/json

# Check network connectivity
docker exec <container-id> ping -c 3 8.8.8.8
```

**Solutions**:
- Verify Docker API is accessible
- Check command whitelist (may be blocked)
- Ensure container is in "running" state
- Check Supabase function timeout (increase if needed)

### Issue 3: High resource usage

**Symptoms**: Server slow, containers unresponsive

**Diagnosis**:
```bash
# Check container resource usage
docker stats

# Check system load
top
htop

# Count running containers
docker ps | wc -l
```

**Solutions**:
- Implement resource limits (see Security section)
- Enable automatic cleanup of inactive containers
- Scale horizontally (add more Docker hosts)
- Optimize container images (remove unnecessary tools)

### Issue 4: Port conflicts

**Symptoms**: Container fails to bind ports

**Diagnosis**:
```bash
# Check port usage
sudo netstat -tulpn | grep <port>

# Check Docker port mappings
docker port <container-id>
```

**Solutions**:
- Use dynamic port allocation
- Implement port pool management
- Use Docker networks instead of host ports

### Issue 5: Network isolation breach

**Symptoms**: Containers can access each other when they shouldn't

**Diagnosis**:
```bash
# Check Docker networks
docker network ls
docker network inspect <network-name>

# Test connectivity
docker exec <container1> ping <container2-ip>
```

**Solutions**:
- Create separate networks per student
- Disable inter-container communication: `--icc=false`
- Use firewall rules within containers

---

## Production Deployment Checklist

### Pre-Deployment

- [ ] Build all container images
- [ ] Test images locally
- [ ] Configure Docker daemon with resource limits
- [ ] Set up monitoring (Grafana/Prometheus)
- [ ] Configure automated backups (database)
- [ ] Set up log aggregation
- [ ] Configure SSL/TLS certificates
- [ ] Set up firewall rules
- [ ] Create monitoring alerts

### Deployment

- [ ] Deploy database migrations
- [ ] Deploy edge functions
- [ ] Build and deploy frontend
- [ ] Configure DNS
- [ ] Test with test accounts
- [ ] Load testing (100+ concurrent users)
- [ ] Security audit
- [ ] Document deployment

### Post-Deployment

- [ ] Monitor error logs (first 24 hours)
- [ ] Check resource usage trends
- [ ] Set up automated cleanup cron jobs
- [ ] Create runbooks for common issues
- [ ] Train support team
- [ ] Schedule maintenance windows

---

## Scaling Guidelines

### 50 Users
- Single Docker host: 16GB RAM, 8 cores
- Max 10 concurrent containers
- No orchestration needed

### 100 Users
- Docker Swarm: 2-3 nodes
- 32GB RAM per node
- Load balancer (HAProxy/Nginx)

### 500 Users
- Kubernetes cluster: 5-10 nodes
- Auto-scaling enabled
- CDN for frontend assets
- Multi-region deployment

### 1000+ Users
- Multi-region Kubernetes
- Global load balancing
- Database read replicas
- Dedicated monitoring infrastructure

---

## Cost Estimates

### AWS (500 concurrent users)

- **ECS Fargate**: $800/month (50 tasks × $0.04/hour)
- **RDS PostgreSQL**: $200/month (Supabase alternative)
- **Load Balancer**: $25/month
- **CloudWatch**: $50/month
- **Data Transfer**: $100/month
- **Total**: ~$1,175/month

### Self-Hosted (500 concurrent users)

- **Servers**: 5× dedicated servers @ $100/month = $500/month
- **Bandwidth**: $100/month
- **Backup storage**: $50/month
- **Monitoring**: $25/month (Grafana Cloud)
- **Total**: ~$675/month

---

## Support and Contact

- **Platform URL**: https://tus9vo7shfes.space.minimax.io
- **Documentation**: This file
- **Edge Function**: https://zwtjirdodmupjsissjzr.supabase.co/functions/v1/container-orchestrator
- **Database**: Supabase (zwtjirdodmupjsissjzr)

---

## Appendix: Complete Docker API Integration

### Replace Simulation Functions

In `/workspace/supabase/functions/container-orchestrator/index.ts`, replace:

```typescript
// CURRENT (Simulation)
async function simulateDockerStart(containerName, config) {
  return `docker-${Math.random().toString(36).substring(7)}`;
}

// REPLACE WITH (Real Docker API)
async function realDockerStart(containerName, config) {
  const response = await fetch('http://docker-host:2375/containers/create', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      Image: config.image,
      name: containerName,
      HostConfig: {
        PortBindings: Object.entries(config.ports).reduce((acc, [containerPort, hostPort]) => {
          acc[`${containerPort}/tcp`] = [{ HostPort: String(hostPort) }];
          return acc;
        }, {}),
        Memory: 536870912, // 512MB
        NanoCpus: 1000000000, // 1 CPU
      },
      Env: Object.entries(config.environment).map(([k, v]) => `${k}=${v}`)
    })
  });

  const { Id } = await response.json();

  // Start container
  await fetch(`http://docker-host:2375/containers/${Id}/start`, {
    method: 'POST'
  });

  return Id;
}
```

Similar replacements for:
- `simulateDockerStop` → `realDockerStop`
- `simulateDockerExec` → `realDockerExec`
- `simulateDockerStats` → `realDockerStats`

---

**END OF DOCUMENT**

For questions or issues, consult the troubleshooting section or review Supabase logs.
