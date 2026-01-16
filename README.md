# AI Traffic Management System

<div align="center">

[![Frontend](https://img.shields.io/badge/frontend-React-61dafb?logo=react&logoColor=white)](https://reactjs.org/)
[![Backend](https://img.shields.io/badge/backend-Flask-000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Vision](https://img.shields.io/badge/vision-YOLOv4-ff6f00)](https://github.com/AlexeyAB/darknet)
[![Optimizer](https://img.shields.io/badge/optimizer-C%2B%2B17-00599c?logo=c%2B%2B&logoColor=white)](https://isocpp.org/)
[![Container](https://img.shields.io/badge/infra-Docker-2496ed?logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<h3>Revolutionizing urban flow with intelligent, adaptive real-time monitoring.</h3>

</div>

---

## 📖 Overview

The **Smart Adaptive Traffic Management System** is an advanced solution designed to optimize traffic flow at intersections. By combining **Computer Vision (YOLOv4)** with **High-Performance Computing (C++)**, the system analyzes real-time video feeds to count vehicles and dynamically adjust traffic signal timings.

**Key Goal:** Minimize congestion and wait times using data-driven decision making.

---

## ✨ Key Features

- **👁️ Real-Time Detection:** Accurate vehicle counting using **YOLOv4**.
- **🧠 AI Optimization:** Genetic algorithms (C++) calculate optimal green light durations.
- **📊 Modern Dashboard:** React-based UI for uploading videos, viewing analytics, and system monitoring.
- **📹 flexible Input:** Supports both uploaded video files and live RTSP camera feeds.
- **🐳 Docker Ready:** Fully containerized for consistent deployment across environments.

---

## 🛠️ Technology Stack

| Component | Tech | Description |
|-----------|------|-------------|
| **Frontend** | React | Responsive dashboard for monitoring & control |
| **Backend** | Flask | REST API to bridge UI and Core Logic |
| **Vision** | YOLOv4 + OpenCV | Object detection & image processing |
| **Core** | C++17 | Genetic Algorithm for signal optimization |
| **DevOps** | Docker | Containerization & Orchestration |

---

## 🚀 Quick Start

### Prerequisites
- [Docker Engine](https://docs.docker.com/engine/install/) & [Docker Compose](https://docs.docker.com/compose/install/)
- **Recommended:** 4GB+ RAM

### ⚡ Installation (The Easy Way)

We use a `Makefile` to simplify common tasks.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/TrafficManagementSystem.git
    cd TrafficManagementSystem
    ```

2.  **Setup & Run:**
    ```bash
    make setup  # Downloads weights & builds images
    make up     # Starts the system
    ```

That's it! The system is now running.

- **Frontend:** [http://localhost:3000](http://localhost:3000)
- **Backend API:** [http://localhost:5000](http://localhost:5000)

### 🕹️ Commands

| Command | Description |
|---------|-------------|
| `make setup` | Prepare environment (download weights, build images) |
| `make up` | Start services in production mode |
| `make dev` | Start services in development mode (hot-reload) |
| `make logs` | Tail logs from all containers |
| `make down` | Stop all services |
| `make help` | Show all available commands |

---

## 🧪 Manual Setup (No Docker)

<details>
<summary>Click to view manual installation steps</summary>

### Backend
1. Navigate to backend: `cd backend`
2. Install Python deps: `pip install -r requirements.txt`
3. Download weights: `bash download.sh`
4. Compile C++ algorithm: `g++ -std=c++17 -O3 -fopenmp -o Algo1 Algo.cpp`
5. Run server: `python app.py`

### Frontend
1. Navigate to frontend: `cd frontend`
2. Install dependencies: `npm install`
3. Start server: `npm start`

</details>

---

## 🤝 Contributing

We welcome contributions!

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/NewFeature`)
3.  Commit your Changes (`git commit -m 'Add NewFeature'`)
4.  Push to the Branch (`git push origin feature/NewFeature`)
5.  Open a Pull Request

---

## 📜 Acknowledgments

- **YOLOv4:** For state-of-the-art object detection.
- **OpenCV:** For powerful image processing capabilities.
- **Darknet:** For the neural network framework.