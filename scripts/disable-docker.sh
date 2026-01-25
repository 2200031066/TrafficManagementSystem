#!/bin/bash

# Script to stop and disable Docker services to free up system resources.

set -e

# Function to display help message
show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Stops and disables Docker services (docker, docker.socket, containerd)."
    echo ""
    echo "Options:"
    echo "  -h, --help    Show this help message and exit"
    echo ""
}

# Parse command line arguments
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    show_help
    exit 0
fi

echo ">>> Docker Service Management"
echo "Stopping Docker services..."

# Stop services
if sudo systemctl stop docker docker.socket containerd; then
    echo " [ OK ] Services stopped."
else
    echo " [FAIL] Failed to stop services."
    exit 1
fi

echo "Disabling Docker auto-start..."
# Disable services
if sudo systemctl disable docker docker.socket containerd; then
    echo " [ OK ] Services disabled."
else
    echo " [FAIL] Failed to disable services."
    exit 1
fi

echo ""
echo ">>> Status Check"
echo "----------------------------------------"

check_status() {
    local service=$1
    if systemctl is-enabled "$service" &>/dev/null; then
        echo -n "[ENABLED]: $service"
    else
        echo -n "[DISABLED]: $service"
    fi
    echo ""
}

check_status "docker"
check_status "docker.socket"
check_status "containerd"

echo ""
echo ">>> Current Status:"
systemctl status docker --no-pager | grep -E "Active | Loader" || true

echo ""
echo " [ DONE ] Docker services have been stopped and disabled."

