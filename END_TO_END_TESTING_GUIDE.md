# End-to-End Testing Guide
# SDN Lab Platform - Real Container Integration

## Overview

This guide provides step-by-step instructions for testing the complete SDN Lab Platform with real Docker container integration and WebSocket streaming.

---

## Prerequisites

Before testing, ensure:
- [ ] Docker host is set up and API is accessible
- [ ] All SDN lab images are built (`sdn-mininet`, `sdn-ryu`, `sdn-ovs`, etc.)
- [ ] Edge functions deployed (`container-orchestrator-production`, `terminal-stream`)
- [ ] Frontend deployed with WebTerminalEnhanced component
- [ ] Network connectivity between all components

---

## Testing Environment

### Server Configuration
- **Docker Host**: Ubuntu 22.04 LTS
- **Docker API**: http://localhost:2375
- **Supabase**: https://zwtjirdodmupjsissjzr.supabase.co
- **Frontend**: https://8rchxdvu6di2.space.minimax.io

### Test Accounts
- **Professor**: dzianikerarti@inttic.dz / karimo2016
- **Student**: alice.chen@students.edu / Student123!

---

## Test Suite

### Phase 1: Infrastructure Tests

#### Test 1.1: Docker API Connectivity
```bash
curl http://localhost:2375/_ping
# Expected: OK
```

**Pass Criteria**: HTTP 200 response

#### Test 1.2: Docker Images
```bash
docker images | grep sdn-
# Expected: List of 5+ SDN images
```

**Pass Criteria**: All required images present (mininet, ryu, ovs, traffic, security)

#### Test 1.3: Docker Network
```bash
docker network inspect sdn-lab-network
# Expected: Network details with bridge driver
```

**Pass Criteria**: Network exists and is accessible

---

### Phase 2: Edge Function Tests

#### Test 2.1: Container Orchestrator - Start Container
```bash
curl -X POST "https://zwtjirdodmupjsissjzr.supabase.co/functions/v1/container-orchestrator-production" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "start",
    "sectionNumber": 0,
    "containerType": "mininet"
  }'
```

**Expected Response**:
```json
{
  "data": {
    "sessionId": "uuid",
    "containerId": "docker-container-id",
    "containerName": "sdn-lab-...",
    "status": "running",
    "ports": {...},
    "message": "Container started successfully"
  }
}
```

**Pass Criteria**: 
- HTTP 200 status
- Valid session ID returned
- Container ID present
- Status = "running"

#### Test 2.2: Execute Command
```bash
curl -X POST "https://zwtjirdodmupjsissjzr.supabase.co/functions/v1/container-orchestrator-production" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "execute",
    "sessionId": "SESSION_ID_FROM_TEST_2.1",
    "command": "mn --version"
  }'
```

**Expected Response**:
```json
{
  "data": {
    "command": "mn --version",
    "output": "Mininet 2.3.0\n",
    "exitCode": 0,
    "timestamp": "2025-11-05T..."
  }
}
```

**Pass Criteria**:
- HTTP 200 status
- Output contains Mininet version
- Exit code = 0

#### Test 2.3: Get Container Status
```bash
curl -X POST "https://zwtjirdodmupjsissjzr.supabase.co/functions/v1/container-orchestrator-production" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "status",
    "sessionId": "SESSION_ID_FROM_TEST_2.1"
  }'
```

**Expected Response**:
```json
{
  "data": {
    "sessionId": "uuid",
    "containerStatus": "running",
    "containerName": "sdn-lab-...",
    "stats": {
      "cpu_percent": "12.50",
      "memory_mb": "256.30",
      "network_rx_bytes": 1024,
      "network_tx_bytes": 512
    }
  }
}
```

**Pass Criteria**:
- HTTP 200 status
- Stats object with CPU/memory metrics
- Container status = "running"

#### Test 2.4: Stop Container
```bash
curl -X POST "https://zwtjirdodmupjsissjzr.supabase.co/functions/v1/container-orchestrator-production" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "stop",
    "sessionId": "SESSION_ID_FROM_TEST_2.1"
  }'
```

**Expected Response**:
```json
{
  "data": {
    "sessionId": "uuid",
    "status": "stopped",
    "message": "Container stopped successfully"
  }
}
```

**Pass Criteria**:
- HTTP 200 status
- Status = "stopped"
- Container removed from Docker

---

### Phase 3: WebSocket Terminal Tests

#### Test 3.1: WebSocket Connection
Use browser Developer Tools to test WebSocket:

1. Open browser console (F12)
2. Navigate to Network tab → WS filter
3. Start container from UI
4. Observe WebSocket connection:

**Expected Events**:
```
Connection opened: wss://zwtjirdodmupjsissjzr.supabase.co/functions/v1/terminal-stream?sessionId=...
Message received: {"type":"ready","message":"Terminal connected"}
```

**Pass Criteria**:
- WebSocket connection established (status 101)
- Ready message received
- Connection stays open

#### Test 3.2: Command Input/Output via WebSocket

In browser console:
```javascript
// Assuming ws is the WebSocket object
ws.send(JSON.stringify({
  type: 'input',
  data: 'echo "Hello SDN"\n',
  rows: 24,
  cols: 80
}));
```

**Expected**:
```
Message received: {"type":"output","data":"echo \"Hello SDN\"\r\n"}
Message received: {"type":"output","data":"Hello SDN\r\n"}
Message received: {"type":"output","data":"$ "}
```

**Pass Criteria**:
- Command echoed back
- Output received in real-time
- Prompt displayed

#### Test 3.3: Terminal Resize

```javascript
ws.send(JSON.stringify({
  type: 'resize',
  rows: 30,
  cols: 100
}));
```

**Pass Criteria**:
- No error response
- Terminal adapts to new size

---

### Phase 4: Frontend Integration Tests

#### Test 4.1: Login and Navigation

**Steps**:
1. Navigate to https://8rchxdvu6di2.space.minimax.io
2. Click "Sign In"
3. Enter student credentials: alice.chen@students.edu / Student123!
4. Click "Sign In"

**Pass Criteria**:
- Successful login
- Redirected to student dashboard
- All 9 lab sections visible

#### Test 4.2: Open Lab Section

**Steps**:
1. Click on "Section 0 - SDN Basics"
2. Verify lab interface loads with 5 tabs

**Pass Criteria**:
- Lab interface displays
- Tabs visible: Tutorial, Terminal, Topology, Flow Tables, Assessment
- Terminal tab is accessible

#### Test 4.3: Start Container from UI

**Steps**:
1. Click "Terminal" tab
2. Observe initial state:
   - Status badge shows "STOPPED"
   - "Start Container" button visible
   - Welcome message in terminal
3. Click "Start Container"
4. Observe status changes:
   - "STARTING" → "RUNNING"
   - WebSocket indicator shows "Connected"
   - Terminal displays container info

**Pass Criteria**:
- Status transitions correctly
- WebSocket connects
- Terminal shows container ID and name
- No errors in browser console

#### Test 4.4: Execute Commands Interactively

**Steps**:
1. Type in terminal: `mn --version`
2. Press Enter
3. Observe output

**Expected Output**:
```
$ mn --version
Mininet 2.3.0
$ 
```

**Pass Criteria**:
- Command appears as typed
- Output displays in real-time
- New prompt appears after output
- No lag or delay (< 200ms)

#### Test 4.5: Test Multiple Commands

**Commands to test**:
```bash
pwd                    # Expected: /root
ls -la                 # Expected: directory listing
ovs-vsctl --version   # Expected: OVS version
ryu-manager --version # Expected: RYU version
ping -c 3 127.0.0.1   # Expected: ping statistics
```

**Pass Criteria**:
- All commands execute successfully
- Output appears in real-time
- Exit codes correct (0 for success)
- No timeout errors

#### Test 4.6: Test Terminal Features

**Tests**:
1. **Backspace**: Type text, press backspace, verify deletion
2. **Ctrl+C**: Run long command, press Ctrl+C, verify interruption
3. **Fullscreen**: Click fullscreen toggle, verify expansion
4. **Resize**: Resize browser window, verify terminal adapts

**Pass Criteria**:
- All keyboard shortcuts work
- Fullscreen mode toggles correctly
- Terminal auto-fits to window size

#### Test 4.7: Stop Container

**Steps**:
1. Click "Stop Container" button
2. Observe:
   - WebSocket disconnects
   - Status changes to "STOPPED"
   - Terminal displays "Container stopped" message

**Pass Criteria**:
- Container stops cleanly
- No orphaned containers in Docker
- Database session updated to "stopped"

---

### Phase 5: Cross-Section Tests

#### Test 5.1: Test All 9 Lab Sections

Repeat Tests 4.3-4.7 for each section:
- Section 0: Mininet
- Section 1: Mininet
- Section 2: RYU
- Section 3: OVS
- Section 4: Mininet
- Section 5: Traffic Analyzer
- Section 6: Custom
- Section 7: RYU
- Section 8: Security Lab

**Pass Criteria**:
- Each section starts appropriate container type
- All containers function independently
- No cross-contamination between sessions

---

### Phase 6: Concurrent User Tests

#### Test 6.1: Multiple Students Simultaneously

**Setup**:
1. Open 3 browsers (or incognito windows)
2. Login as different students in each
3. Start containers in each session simultaneously

**Pass Criteria**:
- All containers start successfully
- Each student has isolated environment
- No resource conflicts
- Each WebSocket connection independent

#### Test 6.2: Load Test (10+ Concurrent Users)

Use load testing tool (e.g., Artillery, k6):

```yaml
# artillery-test.yml
config:
  target: 'https://8rchxdvu6di2.space.minimax.io'
  phases:
    - duration: 60
      arrivalRate: 10
scenarios:
  - name: "Start Lab Container"
    flow:
      - post:
          url: "/functions/v1/container-orchestrator-production"
          json:
            action: "start"
            sectionNumber: 0
            containerType: "mininet"
```

**Pass Criteria**:
- All requests succeed (< 5% error rate)
- Response time < 2 seconds
- No server crashes
- Containers cleaned up after

---

### Phase 7: Error Handling Tests

#### Test 7.1: Invalid Commands

Execute dangerous commands:
```bash
rm -rf /
dd if=/dev/zero of=/dev/sda
:(){ :|:& };:
```

**Pass Criteria**:
- All dangerous commands blocked
- Error message displayed: "Command not allowed"
- Container remains safe

#### Test 7.2: Container Failure Recovery

**Steps**:
1. Start container
2. Manually kill container: `docker kill CONTAINER_ID`
3. Try to execute command in UI

**Pass Criteria**:
- UI detects container is down
- Error message displayed
- Status updates to "error"
- User can restart container

#### Test 7.3: Network Interruption

**Steps**:
1. Start container and WebSocket
2. Disconnect network briefly
3. Reconnect network

**Pass Criteria**:
- WebSocket disconnects gracefully
- UI shows "WebSocket Disconnected"
- Automatic reconnection attempted
- Session recoverable

---

### Phase 8: Database Validation Tests

#### Test 8.1: Session Persistence

**Steps**:
1. Start container
2. Query database:
```sql
SELECT * FROM container_sessions WHERE user_id = 'STUDENT_USER_ID' ORDER BY created_at DESC LIMIT 1;
```

**Pass Criteria**:
- Session record exists
- Status = "running"
- Container ID matches Docker
- Timestamps accurate

#### Test 8.2: Event Logging

**Steps**:
1. Start container, execute commands, stop container
2. Query events:
```sql
SELECT * FROM container_events WHERE container_session_id = 'SESSION_ID' ORDER BY created_at;
```

**Pass Criteria**:
- All events logged (create, start, command_executed, stop)
- Event data contains relevant info
- Timestamps in correct order

#### Test 8.3: Metrics Collection

**Steps**:
1. Start container
2. Wait 60 seconds
3. Query metrics:
```sql
SELECT * FROM container_metrics WHERE container_session_id = 'SESSION_ID' ORDER BY recorded_at DESC LIMIT 5;
```

**Pass Criteria**:
- Metrics recorded periodically
- CPU/memory values realistic
- Network stats increasing

---

## Performance Benchmarks

### Target Metrics
- **Container Start Time**: < 5 seconds
- **Command Execution Latency**: < 200ms
- **WebSocket Latency**: < 50ms
- **Concurrent Users Supported**: 50+ (single server)
- **Memory per Container**: < 512MB
- **CPU per Container**: < 1 core

### Measurement Tools
```bash
# Container start time
time docker start CONTAINER_ID

# Command execution latency
time docker exec CONTAINER_ID echo "test"

# WebSocket latency (use browser DevTools Network tab)
```

---

## Automated Testing Script

Create automated test suite:

```bash
#!/bin/bash
# automated-e2e-test.sh

# Test 1: Docker API
echo "Test 1: Docker API"
curl -s http://localhost:2375/_ping || exit 1
echo "✓ Passed"

# Test 2: Create Container via API
echo "Test 2: Create and Start Container"
CONTAINER_ID=$(curl -s -X POST http://localhost:2375/containers/create \
  -H "Content-Type: application/json" \
  -d '{"Image":"sdn-mininet:latest","Cmd":["sleep","30"]}' | \
  jq -r '.Id')

curl -s -X POST http://localhost:2375/containers/${CONTAINER_ID}/start
sleep 2
echo "✓ Passed: ${CONTAINER_ID:0:12}"

# Test 3: Execute Command
echo "Test 3: Execute Command"
EXEC_ID=$(curl -s -X POST http://localhost:2375/containers/${CONTAINER_ID}/exec \
  -H "Content-Type: application/json" \
  -d '{"AttachStdout":true,"Cmd":["mn","--version"]}' | \
  jq -r '.Id')

OUTPUT=$(curl -s -X POST http://localhost:2375/exec/${EXEC_ID}/start \
  -H "Content-Type: application/json" \
  -d '{"Detach":false}')

if echo "$OUTPUT" | grep -q "Mininet"; then
  echo "✓ Passed: $OUTPUT"
else
  echo "✗ Failed"
  exit 1
fi

# Test 4: Cleanup
echo "Test 4: Cleanup"
curl -s -X POST http://localhost:2375/containers/${CONTAINER_ID}/stop
curl -s -X DELETE http://localhost:2375/containers/${CONTAINER_ID}
echo "✓ Passed"

echo "All tests passed!"
```

---

## Success Criteria Summary

For production readiness, all tests must pass:

- [ ] Infrastructure: Docker API, images, network
- [ ] Edge Functions: All 6 endpoints functional
- [ ] WebSocket: Real-time streaming working
- [ ] Frontend: All UI interactions smooth
- [ ] Cross-Section: All 9 labs functional
- [ ] Concurrent Users: 10+ users supported
- [ ] Error Handling: Graceful failure recovery
- [ ] Database: All operations persisted
- [ ] Performance: Meets benchmarks

---

## Troubleshooting

### Issue: Container fails to start
**Solution**: Check Docker logs, verify image exists, ensure sufficient resources

### Issue: WebSocket won't connect
**Solution**: Verify edge function deployed, check CORS headers, inspect browser console

### Issue: Commands timeout
**Solution**: Check Docker API connectivity, verify container is running, review network latency

### Issue: High memory usage
**Solution**: Implement resource limits, enable cleanup cron job, scale horizontally

---

## Next Steps After Testing

1. **Performance Optimization**: Based on metrics, optimize slow operations
2. **Security Audit**: Review and harden all endpoints
3. **Monitoring Setup**: Deploy Prometheus/Grafana for production
4. **Documentation**: Update user guides with real examples
5. **Training**: Train professors and TAs on platform use

---

**Testing Completed**: [ ]  
**Production Ready**: [ ]  
**Deployment Date**: ___________
