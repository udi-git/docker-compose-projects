# Flask Docker Container Manager

## Overview
This project is a Flask-based web application that provides a simple, user-friendly interface for managing Docker containers on a host server. Users can effortlessly create, view, and delete containers through a responsive web dashboard, abstracting the need for CLI commands.

## Mission
The mission of this project is to create a streamlined tool for Docker container management. Key features include:

* **Container Management:**
  * Create new Docker containers dynamically with user-specified parameters (Name, Image, Host Port, Container Port).
  * View a real-time list of existing containers along with their current status and Short IDs.
  * Delete/Stop containers that are no longer needed directly from the UI.
* **Container Access:**
  * Once a container is running, it is accessible via the host machine using the mapped ports.

## Architecture & Technical Highlights
* **Backend:** Python 3.9 with Flask 3.0.0.
* **Docker Engine API:** Utilizes the official `docker` Python SDK (v7.1.0+) to communicate with the host's Docker daemon.
* **Docker Socket Mounting:** The application itself runs inside a Docker container. It achieves control over the host's Docker daemon by binding the Docker socket (`/var/run/docker.sock:/var/run/docker.sock`) via `docker-compose.yml`.
* **Live Development Volume:** Configured a local bind mount (`.:/app`) in Docker Compose to allow immediate UI and backend code updates without needing to rebuild the image.
* **Frontend:** HTML5 and CSS3 integrated with Jinja2 templating for dynamic data rendering and a responsive flexbox layout.

## Setup & Execution

### Prerequisites
* Docker and Docker Compose installed on your host machine.

### Running the Application
1. Clone this repository and navigate to the root directory.
2. Build and start the infrastructure using Docker Compose:
   ```bash
   docker compose up --build -d
