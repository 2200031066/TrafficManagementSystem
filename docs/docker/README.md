# Docker Deployment Guide

---

# Overview

This guide describes how to deploy the AI Traffic Management System using Docker and Docker Compose.

Containerized deployment ensures:

- Environment consistency
- Simplified setup
- Isolation of dependencies
- Production-ready scalability

> [!IMPORTANT]
> Docker deployment is the recommended method for both development and production environments.

---

# Services

The system runs as two primary containers:

---

## Frontend Container

- **Production Base Image:** `nginx:alpine`
- **Development Base Image:** `node:18`
- **Port Mapping:**
  - Production → `3000:80`
  - Development → `3000:3000`
- **Role:** Serves the React build and proxies API requests (if configured)

### Responsibilities
- Hosts static React build (production)
- Supports hot reload (development)
- Connects to backend via internal Docker network

---

## Backend Container

- **Base Image:** `python:3.10-slim`
- **Port Mapping:** `5000:5000`

### System Dependencies
- `libgl1` (required for OpenCV)
- `libgomp1` (required for OpenMP / C++ optimization)

### Mounted Volumes

Persistent directories:

- `backend/uploads/`
- `backend/outputs/`
- `backend/data/`

> [!IMPORTANT]
> Volume mounting ensures logs, analytics, and uploaded files persist across container restarts.

---

# Setup Instructions

---

## 1. Initial Preparation

Download model weights and build Docker images:

```bash
make setup
```

This step:
- Downloads large YOLO weight files
- Builds frontend and backend images
- Prepares required directories

> [!IMPORTANT]
> Run this step before `make up` to avoid build failures.

---

## 2. Starting Services

### Production Mode

Starts optimized containers in detached mode:

```bash
make up
```

Access services:

- Frontend → http://localhost:3000
- Backend → http://localhost:5000

---

### Development Mode

Starts containers with volume mounting for hot reload:

```bash
make dev
```

Features:
- Live code updates
- Debug-friendly configuration
- Mounted source directories

---

## 3. Stopping Services

Stop and remove running containers:

```bash
make down
```

To remove volumes as well:

```bash
docker compose down -v
```

> [!WARNING]
> Removing volumes will delete persisted data.

---

# Environment Configuration

Environment variables are loaded via `.env` files inside:

- `frontend/`
- `backend/`

---

## Backend Environment Variables

| Variable | Description |
|----------|------------|
| `FLASK_ENV` | Application mode (`development` or `production`) |
| `MAX_UPLOAD_SIZE_MB` | Maximum allowed upload size (default: 200) |

---

## Frontend Environment Variables

| Variable | Description |
|----------|------------|
| `REACT_APP_API_URL` | Backend API base URL |

> [!IMPORTANT]
> All React environment variables must be prefixed with `REACT_APP_`.

---

# Networking

Docker Compose creates an internal bridge network allowing:

- Frontend to communicate with backend using service name
- Isolated inter-container communication
- No need for hardcoded IP addresses

Example internal API URL:

```
http://backend:5000
```

---

# Troubleshooting

---

## Build Failures

- Ensure `make setup` has completed successfully.
- Confirm YOLO weight files exist before building images.
- Clear Docker cache if needed:

```bash
docker builder prune
```

---

## Port Conflicts

If ports `3000` or `5000` are already in use:

```bash
sudo lsof -i :3000
sudo lsof -i :5000
```

Stop conflicting services or modify `docker-compose.yml` port mappings.

---

## Permission Issues

If volume mounting fails:

```bash
sudo chown -R $USER:$USER backend/data
```

Ensure the Docker user has write access to:

- `backend/data`
- `backend/uploads`
- `backend/outputs`

---

## "Works on My Machine" Issue

If the system works locally but fails inside Docker:

Check the following:

- Missing system libraries (OpenCV dependencies)
- Incorrect environment variables
- Hardcoded file paths
- Differences in Python version
- Missing model weight files inside container
- Improper volume mounting

To debug inside container:

```bash
docker exec -it <container_name> bash
```

Inspect logs:

```bash
docker logs <container_name>
```

> [!IMPORTANT]
> Docker containers are isolated environments. Always verify dependencies are installed inside the image, not just on the host system.

---

# Production Recommendations

- Use multi-stage Docker builds for smaller images
- Enable Nginx compression (gzip)
- Use a reverse proxy (Nginx / Traefik)
- Add health checks in `docker-compose.yml`
- Store logs externally for scaling setups

---

# Architecture Summary (Containerized)

```
Browser
   │
   ▼
Frontend Container (Nginx)
   │
   ▼
Backend Container (Flask + C++ + YOLO)
   │
   ▼
Volumes (uploads / outputs / analytics)
```

---

# Recommended Docker Versions

- Docker Engine 20.10+
- Docker Compose 2.0+

> [!IMPORTANT]
> Ensure Docker daemon is running before executing any Makefile commands.
