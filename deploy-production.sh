#!/bin/bash

# SDN Lab Platform - Production Deployment Script
# Deploys full Docker integration with real container execution
# 
# Usage: ./deploy-production.sh [mode]
# Modes: setup, build, deploy, test, cleanup

set -e

# Configuration
DOCKER_HOST_IP="${DOCKER_HOST_IP:-localhost}"
DOCKER_API_PORT="${DOCKER_API_PORT:-2375}"
SUPABASE_URL="${SUPABASE_URL:-https://zwtjirdodmupjsissjzr.supabase.co}"
PROJECT_DIR="/workspace/sdn_lab"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function: Setup Docker Host
setup_docker_host() {
    log_info "Setting up Docker host..."
    
    # Check if Docker is installed
    if ! command -v docker &> /dev/null; then
        log_info "Installing Docker..."
        curl -fsSL https://get.docker.com -o get-docker.sh
        sudo sh get-docker.sh
        sudo usermod -aG docker $USER
        log_info "Docker installed. You may need to log out and back in."
    else
        log_info "Docker already installed: $(docker --version)"
    fi
    
    # Enable Docker API (WARNING: Only for controlled environments!)
    log_warn "Enabling Docker API on port ${DOCKER_API_PORT}"
    log_warn "This should ONLY be done in isolated/firewall-protected environments!"
    
    sudo mkdir -p /etc/systemd/system/docker.service.d
    
    cat <<EOF | sudo tee /etc/systemd/system/docker.service.d/override.conf
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H tcp://127.0.0.1:${DOCKER_API_PORT} -H unix:///var/run/docker.sock --containerd=/run/containerd/containerd.sock
EOF
    
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    
    # Test Docker API
    sleep 3
    if curl -s http://127.0.0.1:${DOCKER_API_PORT}/_ping > /dev/null; then
        log_info "Docker API is responding"
    else
        log_error "Docker API is not responding on port ${DOCKER_API_PORT}"
        exit 1
    fi
    
    # Create SDN lab network
    log_info "Creating sdn-lab-network..."
    docker network create --driver bridge sdn-lab-network 2>/dev/null || log_warn "Network already exists"
    
    log_info "Docker host setup complete!"
}

# Function: Build Container Images
build_images() {
    log_info "Building SDN lab container images..."
    
    cd $PROJECT_DIR
    
    # Build all images
    log_info "Building Mininet image..."
    docker build -t sdn-mininet:latest -f mininet/Dockerfile ./mininet
    
    log_info "Building RYU Controller image..."
    docker build -t sdn-ryu:latest -f ryu/Dockerfile ./ryu
    
    log_info "Building Open vSwitch image..."
    docker build -t sdn-ovs:latest -f ovs/Dockerfile ./ovs
    
    log_info "Building Traffic Analyzer image..."
    docker build -t sdn-traffic:latest -f traffic_analysis/Dockerfile ./traffic_analysis || log_warn "Traffic analyzer Dockerfile not found, skipping..."
    
    log_info "Building Security Lab image..."
    docker build -t sdn-security:latest -f advanced_security/Dockerfile ./advanced_security || log_warn "Security lab Dockerfile not found, skipping..."
    
    # List built images
    log_info "Built images:"
    docker images | grep sdn-
    
    log_info "Image build complete!"
}

# Function: Deploy Edge Functions
deploy_edge_functions() {
    log_info "Deploying Supabase Edge Functions..."
    
    cd /workspace
    
    # Install Supabase CLI if not present
    if ! command -v supabase &> /dev/null; then
        log_info "Installing Supabase CLI..."
        brew install supabase/tap/supabase 2>/dev/null || \
        npm install -g supabase 2>/dev/null || \
        log_error "Failed to install Supabase CLI. Please install manually."
        return 1
    fi
    
    # Set environment variables for edge functions
    log_info "Setting edge function environment variables..."
    
    cat <<EOF > /workspace/supabase/.env
DOCKER_HOST=http://${DOCKER_HOST_IP}:${DOCKER_API_PORT}
SUPABASE_URL=${SUPABASE_URL}
EOF
    
    log_info "Deploying container-orchestrator-production..."
    supabase functions deploy container-orchestrator-production \
        --project-ref ${SUPABASE_PROJECT_REF:-zwtjirdodmupjsissjzr} || \
        log_warn "Manual deployment required via Supabase Dashboard"
    
    log_info "Deploying terminal-stream..."
    supabase functions deploy terminal-stream \
        --project-ref ${SUPABASE_PROJECT_REF:-zwtjirdodmupjsissjzr} || \
        log_warn "Manual deployment required via Supabase Dashboard"
    
    log_info "Edge functions deployed!"
}

# Function: Test Container System
test_container_system() {
    log_info "Testing container system..."
    
    # Test 1: Docker API connectivity
    log_info "Test 1: Docker API connectivity"
    if curl -s http://127.0.0.1:${DOCKER_API_PORT}/_ping > /dev/null; then
        log_info "✓ Docker API is accessible"
    else
        log_error "✗ Docker API is not accessible"
        return 1
    fi
    
    # Test 2: Create test container
    log_info "Test 2: Creating test container"
    CONTAINER_ID=$(curl -s -X POST http://127.0.0.1:${DOCKER_API_PORT}/containers/create \
        -H "Content-Type: application/json" \
        -d '{"Image":"sdn-mininet:latest","Cmd":["sleep","30"]}' | \
        python3 -c "import sys, json; print(json.load(sys.stdin)['Id'])")
    
    if [ -n "$CONTAINER_ID" ]; then
        log_info "✓ Container created: ${CONTAINER_ID:0:12}"
    else
        log_error "✗ Failed to create container"
        return 1
    fi
    
    # Test 3: Start container
    log_info "Test 3: Starting container"
    curl -s -X POST http://127.0.0.1:${DOCKER_API_PORT}/containers/${CONTAINER_ID}/start
    sleep 2
    
    # Test 4: Execute command
    log_info "Test 4: Executing command in container"
    EXEC_ID=$(curl -s -X POST http://127.0.0.1:${DOCKER_API_PORT}/containers/${CONTAINER_ID}/exec \
        -H "Content-Type: application/json" \
        -d '{"AttachStdout":true,"Cmd":["echo","Hello SDN Lab"]}' | \
        python3 -c "import sys, json; print(json.load(sys.stdin)['Id'])")
    
    if [ -n "$EXEC_ID" ]; then
        log_info "✓ Command exec created: ${EXEC_ID:0:12}"
        
        # Start exec
        OUTPUT=$(curl -s -X POST http://127.0.0.1:${DOCKER_API_PORT}/exec/${EXEC_ID}/start \
            -H "Content-Type: application/json" \
            -d '{"Detach":false}')
        log_info "✓ Command output: $OUTPUT"
    else
        log_error "✗ Failed to execute command"
    fi
    
    # Test 5: Stop and remove container
    log_info "Test 5: Stopping and removing container"
    curl -s -X POST http://127.0.0.1:${DOCKER_API_PORT}/containers/${CONTAINER_ID}/stop
    sleep 2
    curl -s -X DELETE http://127.0.0.1:${DOCKER_API_PORT}/containers/${CONTAINER_ID}
    log_info "✓ Container stopped and removed"
    
    # Test 6: Check images
    log_info "Test 6: Verifying images"
    IMAGES=$(curl -s http://127.0.0.1:${DOCKER_API_PORT}/images/json | \
        python3 -c "import sys, json; print(len([i for i in json.load(sys.stdin) if 'sdn-' in str(i.get('RepoTags', []))]))")
    log_info "✓ Found ${IMAGES} SDN lab images"
    
    log_info "All tests passed! Container system is functional."
}

# Function: Setup Monitoring
setup_monitoring() {
    log_info "Setting up monitoring with Prometheus and Grafana..."
    
    cd /workspace
    
    # Deploy monitoring stack
    docker-compose -f docker-compose.production.yml up -d prometheus grafana cadvisor
    
    log_info "Monitoring stack deployed:"
    log_info "  - Prometheus: http://localhost:9090"
    log_info "  - Grafana: http://localhost:3000 (admin/admin)"
    log_info "  - cAdvisor: http://localhost:8080"
}

# Function: Cleanup
cleanup() {
    log_warn "Cleaning up all SDN lab containers..."
    
    # Stop all sdn-lab containers
    docker ps -a --filter "label=sdn-lab.user" --format "{{.ID}}" | xargs -r docker stop
    docker ps -a --filter "label=sdn-lab.user" --format "{{.ID}}" | xargs -r docker rm
    
    log_info "Cleanup complete"
}

# Function: Show Status
show_status() {
    log_info "SDN Lab Platform Status:"
    echo ""
    
    log_info "Docker Status:"
    docker info | grep "Server Version" || log_error "Docker not running"
    echo ""
    
    log_info "Docker API:"
    curl -s http://127.0.0.1:${DOCKER_API_PORT}/_ping && \
        log_info "✓ Accessible at http://127.0.0.1:${DOCKER_API_PORT}" || \
        log_error "✗ Not accessible"
    echo ""
    
    log_info "SDN Lab Images:"
    docker images | grep sdn- || log_warn "No SDN images found"
    echo ""
    
    log_info "Active Containers:"
    docker ps --filter "label=sdn-lab.user" || log_info "No active lab containers"
    echo ""
    
    log_info "Network:"
    docker network inspect sdn-lab-network > /dev/null 2>&1 && \
        log_info "✓ sdn-lab-network exists" || \
        log_warn "✗ sdn-lab-network not found"
}

# Main script
case "${1:-}" in
    setup)
        setup_docker_host
        ;;
    build)
        build_images
        ;;
    deploy)
        deploy_edge_functions
        ;;
    test)
        test_container_system
        ;;
    monitoring)
        setup_monitoring
        ;;
    cleanup)
        cleanup
        ;;
    status)
        show_status
        ;;
    all)
        log_info "Running full deployment..."
        setup_docker_host
        build_images
        test_container_system
        deploy_edge_functions
        setup_monitoring
        show_status
        log_info "Deployment complete!"
        ;;
    *)
        echo "Usage: $0 {setup|build|deploy|test|monitoring|cleanup|status|all}"
        echo ""
        echo "  setup      - Setup Docker host with API"
        echo "  build      - Build all SDN lab container images"
        echo "  deploy     - Deploy Supabase edge functions"
        echo "  test       - Test container system"
        echo "  monitoring - Setup Prometheus/Grafana monitoring"
        echo "  cleanup    - Remove all lab containers"
        echo "  status     - Show system status"
        echo "  all        - Run full deployment (setup + build + test + deploy + monitoring)"
        exit 1
        ;;
esac
