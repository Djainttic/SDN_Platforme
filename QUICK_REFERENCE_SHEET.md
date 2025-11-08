# SDN Lab Platform - Quick Reference Sheet

**Version**: 1.0 Production Release  
**Date**: 2025-11-05

---

## Essential URLs

**Platform**: https://377u4geo9kkl.space.minimax.io  
**Supabase Dashboard**: https://supabase.com/dashboard/project/zwtjirdodmupjsissjzr  
**Project ID**: zwtjirdodmupjsissjzr

---

## Access Credentials

**Professor**:
- Email: dzianikerarti@inttic.dz
- Password: karimo2016

**Test Student**:
- Email: alice.chen@students.edu
- Password: Student123!

---

## Edge Functions

1. **container-orchestrator-production** (ACTIVE)
   - ID: f7eaba7b-b91c-4766-a5d8-a188f4bd302c
   - URL: https://zwtjirdodmupjsissjzr.supabase.co/functions/v1/container-orchestrator-production

2. **terminal-stream** (ACTIVE)
   - ID: fda2d929-7d93-4a2c-aceb-dc5b2c407e5b
   - URL: wss://zwtjirdodmupjsissjzr.supabase.co/functions/v1/terminal-stream

---

## Platform Statistics

- **Lab Sections**: 9 complete sections
- **Tutorial Steps**: 85 across all sections
- **Quiz Questions**: 113 total
- **Exercises**: 63 hands-on tasks
- **Database Tables**: 25 tables
- **Edge Functions**: 15+ deployed
- **Documentation**: 5,100+ lines

---

## Documentation Files

Located in `/workspace/`:

1. **PROFESSOR_USER_GUIDE.md** (720 lines)
   - Complete professor manual
   - Class and student management
   - Grading and analytics

2. **STUDENT_USER_GUIDE.md** (783 lines)
   - Student walkthrough
   - Lab instructions
   - Command reference

3. **DOCKER_HOST_SETUP_GUIDE.md** (1,030 lines)
   - Docker installation
   - Container building
   - Network configuration

4. **FINAL_DEPLOYMENT_SUMMARY.md** (785 lines)
   - Complete platform overview
   - Architecture details
   - Deployment checklist

5. **FINAL_VALIDATION_REPORT.md** (595 lines)
   - Validation results
   - Quality metrics
   - Recommendations

6. **CONTAINER_INTEGRATION_GUIDE.md** (892 lines)
   - Technical deep dive
   - API specifications
   - Troubleshooting

---

## Quick Setup (Docker Host)

### Prerequisites
- Ubuntu 22.04 LTS
- 4 CPU cores, 16 GB RAM, 100 GB storage
- Sudo access

### Installation Steps

```bash
# 1. Install Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# 2. Create network
docker network create sdn-lab-network

# 3. Build images (from project directory)
cd ~/sdn-lab-platform/sdn_lab
docker-compose build

# 4. Verify images
docker images | grep sdn-

# 5. Test container
docker run --rm --privileged sdn-mininet:latest mn --version
```

### Configure Supabase

1. Go to Supabase Dashboard
2. Navigate to Edge Functions → Environment Variables
3. Add: `DOCKER_HOST = unix:///var/run/docker.sock` or `http://YOUR_IP:2375`
4. Redeploy functions

### Test End-to-End

1. Login to platform
2. Open lab section → Terminal tab
3. Click "Start Container"
4. Execute: `mn --version`
5. Verify output appears
6. Click "Stop Container"

**Estimated Time**: 2-4 hours

---

## Container Types

| Type | Image | Sections | Tools |
|------|-------|----------|-------|
| Mininet | sdn-mininet:latest | 0,1,4,6 | Mininet, OVS |
| RYU | sdn-ryu:latest | 2,7 | RYU Controller |
| OVS | sdn-ovs:latest | 3 | Open vSwitch |
| Traffic | sdn-traffic:latest | 5 | tcpdump, iperf, Wireshark |
| Security | sdn-security:latest | 8 | Security tools |

---

## Resource Limits

**Per Container**:
- CPU: 1 core
- Memory: 512 MB
- Disk: 5 GB
- Timeout: 60 minutes

**Server Capacity**:
- Minimum (16GB RAM): ~12 concurrent containers
- Recommended (32GB RAM): ~48 concurrent containers

---

## Common Commands

### Docker Management
```bash
# List containers
docker ps

# Stop container
docker stop <container_id>

# View logs
docker logs <container_id>

# Clean up
docker container prune -f
docker system prune -a
```

### Platform Monitoring
```bash
# Check container count
docker ps -q | wc -l

# Monitor resources
docker stats

# View disk usage
docker system df
```

---

## Troubleshooting Quick Fixes

### Container Won't Start
```bash
sudo systemctl restart docker
docker container prune -f
```

### High Resource Usage
```bash
# Stop inactive containers
docker ps -a | grep Exited | awk '{print $1}' | xargs docker rm

# Check resource usage
free -h
df -h
```

### API Connection Failed
```bash
# Test Docker API
curl --unix-socket /var/run/docker.sock http://localhost/version

# Verify environment variable in Supabase
# Check Edge Functions → Environment Variables
```

---

## Support Contacts

**Platform Issues**:
- Review: PROFESSOR_USER_GUIDE.md or STUDENT_USER_GUIDE.md
- Check: FINAL_VALIDATION_REPORT.md

**Technical Setup**:
- Review: DOCKER_HOST_SETUP_GUIDE.md
- Check: CONTAINER_INTEGRATION_GUIDE.md

**Deployment Questions**:
- Review: FINAL_DEPLOYMENT_SUMMARY.md

---

## Lab Section Reference

| # | Topic | Time | Difficulty |
|---|-------|------|------------|
| 0 | Introduction to SDN | 2-3h | Beginner |
| 1 | Mininet Basics | 2-4h | Beginner |
| 2 | RYU Controller | 3-4h | Intermediate |
| 3 | Open vSwitch | 3-4h | Intermediate |
| 4 | OpenFlow Protocol | 3-5h | Intermediate |
| 5 | Traffic Analysis | 2-3h | Intermediate |
| 6 | Custom Topologies | 4-5h | Advanced |
| 7 | Controller Applications | 4-6h | Advanced |
| 8 | SDN Security | 3-5h | Advanced |

**Total Course Time**: 25-35 hours

---

## System Requirements

**Server (Docker Host)**:
- OS: Ubuntu 22.04 LTS
- CPU: 4+ cores (8+ recommended)
- RAM: 16+ GB (32+ recommended)
- Storage: 100+ GB SSD
- Network: 100 Mbps (1 Gbps recommended)

**Client (Students/Professors)**:
- Browser: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- Internet: 5+ Mbps (10+ Mbps recommended)
- Display: 1280x720 (1920x1080 recommended)

---

## Status Indicators

**Platform**: ✓ LIVE  
**Frontend**: ✓ DEPLOYED  
**Backend**: ✓ ACTIVE  
**Database**: ✓ CONFIGURED  
**Documentation**: ✓ COMPLETE  
**Docker Host**: ⚠ PENDING SETUP

---

## Next Actions Checklist

- [ ] Review documentation (PROFESSOR_USER_GUIDE.md, DOCKER_HOST_SETUP_GUIDE.md)
- [ ] Provision Docker host server
- [ ] Install Docker and build images
- [ ] Configure DOCKER_HOST in Supabase
- [ ] Test end-to-end with real containers
- [ ] Set up monitoring (Prometheus/Grafana - optional)
- [ ] Onboard professors and students
- [ ] Create initial classes for semester

**Estimated Total Time**: 4-6 hours for complete setup

---

## Important Notes

1. **Platform is LIVE**: Accessible at https://377u4geo9kkl.space.minimax.io
2. **Containers need Docker host**: See DOCKER_HOST_SETUP_GUIDE.md
3. **All content complete**: 9 sections with 261 educational items
4. **Production-ready code**: No placeholders, all authentic content
5. **Comprehensive documentation**: 5,100+ lines of guides

---

## Quick Start Commands

### For System Administrator
```bash
# Setup Docker host
curl -fsSL https://get.docker.com | sh
docker network create sdn-lab-network
cd /path/to/project && docker-compose build
# Then configure DOCKER_HOST in Supabase
```

### For Professors
```
1. Login: https://377u4geo9kkl.space.minimax.io
2. Read: PROFESSOR_USER_GUIDE.md
3. Create class
4. Enroll students
5. Monitor progress
```

### For Students
```
1. Login: https://377u4geo9kkl.space.minimax.io
2. Read: STUDENT_USER_GUIDE.md
3. Complete sections 0-8 sequentially
4. Use terminal for hands-on practice
5. Submit assessments
```

---

**End of Quick Reference Sheet**

For detailed information, refer to the comprehensive guides in `/workspace/`.

**Last Updated**: 2025-11-05  
**Platform Version**: 1.0
